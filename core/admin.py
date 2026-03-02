from django.contrib import admin
from django.utils.html import format_html
from .models import AcademyInfo, Course, SuccessStory, GalleryImage, ContactMessage


@admin.register(AcademyInfo)
class AcademyInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('नाव व टॅगलाइन', {'fields': ('name_mr', 'name_en', 'tagline_mr', 'tagline_en')}),
        ('संपर्क', {'fields': ('phone', 'whatsapp', 'email', 'address_mr', 'address_en')}),
        ('मीडिया', {'fields': ('logo', 'hero_image', 'about_image')}),
        ('आमच्याविषयी', {'fields': ('about_text_mr', 'about_text_en', 'established_year')}),
        ('आकडेवारी', {'fields': ('students_selected', 'army_selected', 'police_selected')}),
        ('नकाशा', {'fields': ('google_map_embed',)}),
        ('SEO', {'fields': ('meta_keywords', 'meta_description')}),
    )

    def has_add_permission(self, request):
        return not AcademyInfo.objects.exists()


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'category', 'duration', 'fee', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    list_editable = ['is_active', 'order', 'fee']
    search_fields = ['name_en', 'name_mr']


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'rank_post', 'category', 'year', 'village', 'is_featured']
    list_filter = ['category', 'year', 'is_featured']
    list_editable = ['is_featured']
    search_fields = ['name', 'rank_post', 'village']

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" height="50"/>', obj.photo.url)
        return '—'
    photo_preview.short_description = 'फोटो'
    readonly_fields = ['photo_preview']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_preview', 'uploaded_at']
    list_filter = ['category']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50"/>', obj.image.url)
        return '—'
    image_preview.short_description = 'प्रिव्यू'
    readonly_fields = ['image_preview']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    readonly_fields = ['name', 'mobile', 'email', 'message', 'created_at']
    search_fields = ['name', 'mobile']
