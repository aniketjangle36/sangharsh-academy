from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Course


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'army_training', 'police_training',
                'courses_fees', 'past_results', 'gallery', 'facilities',
                'contact', 'bharti_list']

    def location(self, item):
        return reverse(item)


class CourseSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Course.objects.filter(is_active=True)
