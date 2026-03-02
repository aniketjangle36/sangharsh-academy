from django.contrib import admin
from .models import Bharti


@admin.register(Bharti)
class BhartiAdmin(admin.ModelAdmin):
    list_display = ['title_short', 'category', 'last_date', 'is_active', 'scraped_at']
    list_filter = ['category', 'is_active', 'last_date']
    list_editable = ['is_active', 'category']
    search_fields = ['title', 'short_desc']
    date_hierarchy = 'scraped_at'

    def title_short(self, obj):
        return obj.title[:80] + '...' if len(obj.title) > 80 else obj.title
    title_short.short_description = 'शीर्षक'
