"""
Management command: scrape_bhartis
Fixed for 403 Forbidden + majhinaukri.in structure (h3 + a + p for last date)
"""

import logging
import re
from datetime import datetime
from urllib.parse import urljoin

from django.core.management.base import BaseCommand
from django.utils import timezone

from bharti.models import Bharti

try:
    import cloudscraper
    from bs4 import BeautifulSoup
    SCRAPING_AVAILABLE = True
except ImportError:
    SCRAPING_AVAILABLE = False

logger = logging.getLogger('bharti')

# Keywords
ARMY_KEYWORDS = [
    'आर्मी', 'army', 'agniveer', 'अग्निवीर', 'सैन्य', 'sainya',
    'nda', 'territorial army', 'indian army', 'capf', 'crpf', 'bsf',
    'cisf', 'itbp', 'ssb', 'military', 'defence', 'sainik',
    'zro pune', 'cee', 'women agniveer', 'agniveer women', '2026'
]

POLICE_KEYWORDS = [
    'पोलीस', 'police', 'constable', 'srpf', 'महाराष्ट्र पोलीस',
    'maharashtra police', 'si ', 'sub inspector', 'psi', 'asst',
    'home guard', 'rakshak', 'रक्षक', 'शिपाई', 'capf'
]

SCRAPE_URLS = [
    'https://majhinaukri.in/latest-jobs/',
    'https://majhinaukri.in/police-bharti/',
]


def categorize(title: str) -> str:
    t = title.lower()
    if any(k.lower() in t for k in ARMY_KEYWORDS):
        return 'army'
    if any(k.lower() in t for k in POLICE_KEYWORDS):
        if 'maharashtra' in t or 'महाराष्ट्र' in t:
            return 'maha_police'
        return 'police'
    return 'general'


def parse_date(text: str):
    if not text:
        return None
    text = text.lower().replace('last date:', '').replace('अंतिम तारीख:', '').strip()
    month_map = {
        'january':1, 'jan':1, 'जानेवारी':1,
        'february':2, 'feb':2, 'फेब्रुवारी':2,
        'march':3, 'mar':3, 'मार्च':3,
        'april':4, 'apr':4, 'एप्रिल':4,
        'may':5, 'मे':5,
        'june':6, 'जून':6,
        'july':7, 'जुलै':7,
        'august':8, 'ऑगस्ट':8,
        'september':9, 'सप्टेंबर':9,
        'october':10, 'ऑक्टोबर':10,
        'november':11, 'नोव्हेंबर':11,
        'december':12, 'डिसेंबर':12,
    }
    patterns = [
        r'(\d{1,2})\s+([a-z\u0900-\u097f]+)\s+(\d{4})',
        r'(\d{1,2})[/-](\d{1,2})[/-](\d{4})',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I | re.U)
        if m:
            try:
                groups = m.groups()
                if len(groups) == 3 and any(c.isalpha() or '\u0900' <= c <= '\u097f' for c in groups[1]):
                    day = int(groups[0])
                    month_str = groups[1].lower()
                    year = int(groups[2])
                    month = month_map.get(month_str)
                    if month:
                        return datetime(year, month, day).date()
                elif len(groups) == 3:
                    return datetime(int(groups[2]), int(groups[1]), int(groups[0])).date()
            except:
                pass
    return None


def scrape_url(url: str) -> list:
    jobs = []
    try:
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'chrome',
            'platform': 'windows',
            'mobile': False
        })
        resp = scraper.get(url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Majhinaukri.in structure: <h3><a>title</a></h3> followed by <p>Last Date: ...</p>
        h3_tags = soup.find_all('h3')
        for h3 in h3_tags:
            a_tag = h3.find('a', href=True)
            if not a_tag:
                continue

            title = a_tag.get_text(strip=True)
            if len(title) < 15:
                continue

            link = urljoin(url, a_tag['href'])

            # Find next sibling p or text for date/desc
            desc = ''
            date_text = None
            next_p = h3.find_next_sibling(['p', 'div', 'span'])
            if next_p:
                desc = next_p.get_text(strip=True)[:400]
                # Extract date from desc
                date_match = re.search(r'(?:last date|अंतिम तारीख)[\s:-]*([\d\s]+[a-z\u0900-\u097f]+\s*\d{4}|[\d/-]+)', desc.lower(), re.I | re.U)
                if date_match:
                    date_text = date_match.group(1).strip()

            # Keyword filter
            if not any(k.lower() in title.lower() for k in ARMY_KEYWORDS + POLICE_KEYWORDS):
                continue

            jobs.append({
                'title': title[:500],
                'url': link,
                'short_desc': desc,
                'category': categorize(title),
                'last_date': parse_date(date_text or desc),
            })

    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")

    return jobs


class Command(BaseCommand):
    help = 'Scrape latest bharti from majhinaukri.in with Cloudflare bypass'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true', help='Print only, no save')
        parser.add_argument('--limit', type=int, default=30, help='Max jobs')

    def handle(self, *args, **options):
        if not SCRAPING_AVAILABLE:
            self.stderr.write(self.style.ERROR('Install cloudscraper + requests + beautifulsoup4'))
            return

        self.stdout.write(self.style.SUCCESS('🔍 Starting scrape with bypass...'))

        total_new = 0
        total_skipped = 0
        dry_run = options['dry_run']
        limit = options['limit']

        for url in SCRAPE_URLS:
            self.stdout.write(f'Scraping: {url}')
            jobs = scrape_url(url)
            self.stdout.write(f'  Found {len(jobs)} relevant jobs')

            for job in jobs[:limit]:
                if dry_run:
                    date_str = job['last_date'].strftime('%d %b %Y') if job['last_date'] else 'No date'
                    self.stdout.write(
                        self.style.SUCCESS(f"  [DRY] {job['category'].upper()} | {job['title'][:70]} | Last: {date_str} | {job['url']}")
                    )
                    total_new += 1
                    continue

                obj, created = Bharti.objects.get_or_create(
                    url=job['url'],
                    defaults={
                        'title': job['title'],
                        'category': job['category'],
                        'short_desc': job['short_desc'],
                        'last_date': job['last_date'],
                        'is_active': True,
                        'scraped_at': timezone.now(),
                    }
                )
                if created:
                    total_new += 1
                    logger.info(f"Added: {obj.title[:60]}")
                else:
                    total_skipped += 1

        summary = f'Complete! New: {total_new} | Skipped: {total_skipped}'
        self.stdout.write(self.style.SUCCESS(summary))