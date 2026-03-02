# 🏫 संघर्ष करिअर अकॅडमी फुलंब्री – Django Website

## Project Structure
```
sangharsh_academy/
├── manage.py
├── requirements.txt
├── .env.example
├── sangharsh_academy/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                  ← Main app (Home, About, Courses, Gallery, Contact)
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   ├── sitemaps.py
│   ├── migrations/
│   └── templates/core/
├── bharti/                ← Bharti Updates app
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── management/commands/scrape_bhartis.py
│   └── templates/bharti/
├── templates/
│   └── base.html          ← Main base template
└── static/                ← CSS, JS, Images
```

---

## 🚀 Local Setup (Step-by-Step)

### 1. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate         # Mac/Linux
venv\Scripts\activate            # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create .env file
```bash
cp .env.example .env
# Edit .env with your settings
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## 📢 Scraping Bharti Updates

### Manual Run
```bash
python manage.py scrape_bhartis
python manage.py scrape_bhartis --dry-run   # Test without saving
```

### Cron Job (Daily 11 PM)
```bash
crontab -e
# Add:
0 23 * * * /path/to/venv/bin/python /path/to/manage.py scrape_bhartis >> /path/to/logs/scraper.log 2>&1
```

---

## ☁️ Deployment on Render.com

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Sangharsh Academy"
git remote add origin https://github.com/yourusername/sangharsh-academy.git
git push -u origin main
```

### 2. Create Render Web Service
- Go to render.com → New → Web Service
- Connect your GitHub repo
- Settings:
  - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
  - **Start Command:** `gunicorn sangharsh_academy.wsgi:application`
  - **Environment:** Python 3.11

### 3. Add Environment Variables in Render
```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
DATABASE_URL=postgresql://...  (from Render PostgreSQL)
```

### 4. Add PostgreSQL
- Render Dashboard → New → PostgreSQL
- Copy DATABASE_URL to your web service's env vars

---

## ☁️ Deployment on Railway.app

```bash
# Install Railway CLI
npm install -g @railway/cli
railway login
railway init
railway add --plugin postgresql
railway up
```

Set env vars:
```
SECRET_KEY=...
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

---

## 🔧 Admin Panel Usage

1. Go to `/admin`
2. Login with superuser credentials
3. **अकॅडमी माहिती** – Update academy name, phone, WhatsApp, address
4. **कोर्सेस** – Add Army/Police courses with fees
5. **यशोगाथा** – Add student success stories with photos
6. **भरती** – Manually add or view scraped bharti notifications
7. **गॅलरी** – Upload training/event photos
8. **संपर्क संदेश** – View contact form submissions

---

## 📱 Features

- ✅ Full Marathi + English dual language content
- ✅ Responsive Mobile-First Design (Tailwind CSS)
- ✅ Auto-scraping bharti from majhinaukri.in
- ✅ WhatsApp floating button
- ✅ Google Map embed
- ✅ Admin panel with custom branding
- ✅ Contact form with Django messages
- ✅ Sitemap for SEO (/sitemap.xml)
- ✅ Achievement counters animation
- ✅ Gallery with lightbox
- ✅ Success stories with rank badges

---

## 🎨 Color Palette

| Color | Hex |
|-------|-----|
| Saffron | #FF9933 |
| Army Green | #006400 |
| Navy Blue | #002366 |
| White | #FFFFFF |
