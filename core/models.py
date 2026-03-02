from django.db import models
from django.utils.translation import gettext_lazy as _


class AcademyInfo(models.Model):
    """Single-instance model for academy details"""
    name_mr = models.CharField(_('नाव (मराठी)'), max_length=200, default='संघर्ष करिअर अकॅडमी फुलंब्री')
    name_en = models.CharField(_('Name (English)'), max_length=200, default='Sangharsh Career Academy Fulambri')
    tagline_mr = models.CharField(_('टॅगलाइन (मराठी)'), max_length=300, default='आर्मी व पोलीस भरती पूर्व प्रशिक्षण केंद्र')
    tagline_en = models.CharField(_('Tagline (English)'), max_length=300, default='Army & Police Pre-Recruitment Training Centre')
    address_mr = models.TextField(_('पत्ता (मराठी)'), default='ता. फुलंब्री, जि. छत्रपती संभाजीनगर, महाराष्ट्र')
    address_en = models.TextField(_('Address (English)'), default='Tal. Fulambri, Dist. Chhatrapati Sambhajinagar, Maharashtra')
    phone = models.CharField(_('फोन'), max_length=20, default='+91 XXXXX XXXXX')
    whatsapp = models.CharField(_('WhatsApp'), max_length=20, default='+91XXXXXXXXXX')
    email = models.EmailField(_('ईमेल'), blank=True)
    established_year = models.IntegerField(_('स्थापना वर्ष'), default=2018)
    logo = models.ImageField(_('लोगो'), upload_to='academy/', blank=True)
    hero_image = models.ImageField(_('Hero Image'), upload_to='academy/', blank=True)
    about_image = models.ImageField(_('About Image'), upload_to='academy/', blank=True)
    about_text_mr = models.TextField(_('आमच्याविषयी (मराठी)'), blank=True)
    about_text_en = models.TextField(_('About Us (English)'), blank=True)
    google_map_embed = models.TextField(_('Google Map Embed Code'), blank=True)
    students_selected = models.IntegerField(_('एकूण निवड'), default=500)
    army_selected = models.IntegerField(_('आर्मी निवड'), default=50)
    police_selected = models.IntegerField(_('पोलीस निवड'), default=200)
    meta_keywords = models.CharField(max_length=500, blank=True, default='army bharti, police bharti, Fulambri, संघर्ष अकॅडमी')
    meta_description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('अकॅडमी माहिती')
        verbose_name_plural = _('अकॅडमी माहिती')

    def __str__(self):
        return self.name_en

    def save(self, *args, **kwargs):
        # Enforce single instance
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)

    @classmethod
    def get_info(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Course(models.Model):
    CATEGORY_CHOICES = [
        ('army', 'आर्मी (Army)'),
        ('police', 'पोलीस (Police)'),
    ]
    DURATION_CHOICES = [
        ('3months', '3 महिने'),
        ('6months', '6 महिने'),
        ('1year', '1 वर्ष'),
        ('2years', '2 वर्षे'),
    ]

    name_mr = models.CharField(_('कोर्स नाव (मराठी)'), max_length=200)
    name_en = models.CharField(_('Course Name (English)'), max_length=200)
    category = models.CharField(_('प्रकार'), max_length=20, choices=CATEGORY_CHOICES)
    duration = models.CharField(_('कालावधी'), max_length=20, choices=DURATION_CHOICES)
    fee = models.DecimalField(_('फी (₹)'), max_digits=8, decimal_places=2)
    description_mr = models.TextField(_('वर्णन (मराठी)'), blank=True)
    description_en = models.TextField(_('Description (English)'), blank=True)
    eligibility_mr = models.TextField(_('पात्रता (मराठी)'), blank=True)
    eligibility_en = models.TextField(_('Eligibility (English)'), blank=True)
    subjects = models.TextField(_('विषय'), blank=True, help_text='Comma separated')
    image = models.ImageField(_('फोटो'), upload_to='courses/', blank=True)
    is_active = models.BooleanField(_('सक्रिय'), default=True)
    order = models.IntegerField(_('क्रम'), default=0)

    class Meta:
        verbose_name = _('कोर्स')
        verbose_name_plural = _('कोर्सेस')
        ordering = ['order', 'name_en']

    def __str__(self):
        return f"{self.name_en} ({self.get_category_display()})"

    def get_subjects_list(self):
        return [s.strip() for s in self.subjects.split(',') if s.strip()]


class SuccessStory(models.Model):
    name = models.CharField(_('नाव'), max_length=100)
    photo = models.ImageField(_('फोटो'), upload_to='success/', blank=True)
    rank_post = models.CharField(_('पद / रँक'), max_length=100)
    category = models.CharField(_('प्रकार'), max_length=20, choices=[('army', 'Army'), ('police', 'Police')])
    year = models.IntegerField(_('वर्ष'))
    village = models.CharField(_('गाव'), max_length=100, blank=True)
    testimonial_mr = models.TextField(_('अभिप्राय (मराठी)'), blank=True)
    testimonial_en = models.TextField(_('Testimonial (English)'), blank=True)
    is_featured = models.BooleanField(_('फीचर'), default=False)

    class Meta:
        verbose_name = _('यशोगाथा')
        verbose_name_plural = _('यशोगाथा')
        ordering = ['-year', 'name']

    def __str__(self):
        return f"{self.name} - {self.rank_post} ({self.year})"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('training', 'Training'),
        ('events', 'Events'),
        ('results', 'Results'),
        ('infrastructure', 'Infrastructure'),
    ]
    title = models.CharField(_('शीर्षक'), max_length=200, blank=True)
    image = models.ImageField(_('फोटो'), upload_to='gallery/')
    category = models.CharField(_('श्रेणी'), max_length=30, choices=CATEGORY_CHOICES, default='training')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('गॅलरी फोटो')
        verbose_name_plural = _('गॅलरी')
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or f"Image {self.pk}"


class ContactMessage(models.Model):
    name = models.CharField(_('नाव'), max_length=100)
    mobile = models.CharField(_('मोबाईल'), max_length=15)
    email = models.EmailField(_('ईमेल'), blank=True)
    message = models.TextField(_('संदेश'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('संपर्क संदेश')
        verbose_name_plural = _('संपर्क संदेश')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.mobile} ({self.created_at.date()})"
