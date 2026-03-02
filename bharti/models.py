from django.db import models
from django.utils.translation import gettext_lazy as _


class Bharti(models.Model):
    CATEGORY_CHOICES = [
        ('army', 'आर्मी / Army'),
        ('police', 'पोलीस / Police'),
        ('maha_police', 'महाराष्ट्र पोलीस'),
        ('general', 'सामान्य / General'),
    ]

    title = models.CharField(_('शीर्षक'), max_length=500)
    url = models.URLField(_('लिंक'), unique=True)
    category = models.CharField(_('श्रेणी'), max_length=20, choices=CATEGORY_CHOICES, default='general')
    short_desc = models.TextField(_('थोडक्यात माहिती'), blank=True)
    last_date = models.DateField(_('शेवटची तारीख'), null=True, blank=True)
    scraped_at = models.DateTimeField(_('स्क्रेप वेळ'), auto_now_add=True)
    is_active = models.BooleanField(_('सक्रिय'), default=True)

    class Meta:
        verbose_name = _('भरती')
        verbose_name_plural = _('भरती अपडेट्स')
        ordering = ['-scraped_at']

    def __str__(self):
        return self.title[:80]
