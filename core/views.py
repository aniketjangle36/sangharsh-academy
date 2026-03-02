from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView

from .models import AcademyInfo, Course, SuccessStory, GalleryImage, ContactMessage
from bharti.models import Bharti


def get_academy_info():
    return AcademyInfo.get_info()


def home(request):
    """Home page with hero, achievements, courses, testimonials"""
    academy = get_academy_info()
    army_courses = Course.objects.filter(category='army', is_active=True)[:3]
    police_courses = Course.objects.filter(category='police', is_active=True)[:3]
    featured_stories = SuccessStory.objects.filter(is_featured=True)[:6]
    recent_bhartis = Bharti.objects.filter(is_active=True)[:4]
    gallery_images = GalleryImage.objects.all()[:8]

    context = {
        'page_title': f"{academy.name_mr} – {academy.tagline_mr}",
        'meta_desc': academy.meta_description or academy.tagline_en,
        'academy': academy,
        'army_courses': army_courses,
        'police_courses': police_courses,
        'featured_stories': featured_stories,
        'recent_bhartis': recent_bhartis,
        'gallery_images': gallery_images,
    }
    return render(request, 'core/home.html', context)


def about(request):
    academy = get_academy_info()
    context = {
        'page_title': 'आमच्याविषयी | About Us',
        'meta_desc': 'Sangharsh Career Academy Fulambri - Army & Police Training Centre in Chhatrapati Sambhajinagar',
        'academy': academy,
    }
    return render(request, 'core/about.html', context)


def army_training(request):
    courses = Course.objects.filter(category='army', is_active=True)
    academy = get_academy_info()
    context = {
        'page_title': 'आर्मी प्रशिक्षण | Army Training',
        'meta_desc': 'Army Agniveer, NDA training at Sangharsh Academy Fulambri',
        'courses': courses,
        'category': 'army',
        'academy': academy,
    }
    return render(request, 'core/training.html', context)


def police_training(request):
    courses = Course.objects.filter(category='police', is_active=True)
    academy = get_academy_info()
    context = {
        'page_title': 'पोलीस प्रशिक्षण | Police Training',
        'meta_desc': 'Maharashtra Police Constable, PSI training at Sangharsh Academy Fulambri',
        'courses': courses,
        'category': 'police',
        'academy': academy,
    }
    return render(request, 'core/training.html', context)


def courses_fees(request):
    army_courses = Course.objects.filter(category='army', is_active=True)
    police_courses = Course.objects.filter(category='police', is_active=True)
    academy = get_academy_info()
    context = {
        'page_title': 'कोर्सेस आणि फी | Courses & Fees',
        'meta_desc': 'Complete course list and fee structure at Sangharsh Career Academy Fulambri',
        'army_courses': army_courses,
        'police_courses': police_courses,
        'academy': academy,
    }
    return render(request, 'core/courses_fees.html', context)


def past_results(request):
    army_stories = SuccessStory.objects.filter(category='army').order_by('-year')
    police_stories = SuccessStory.objects.filter(category='police').order_by('-year')
    academy = get_academy_info()
    context = {
        'page_title': 'मागील निकाल | Past Results & Success Stories',
        'meta_desc': '500+ students selected in Army & Police from Sangharsh Academy Fulambri',
        'army_stories': army_stories,
        'police_stories': police_stories,
        'academy': academy,
    }
    return render(request, 'core/past_results.html', context)


def gallery(request):
    category_filter = request.GET.get('cat', '')
    images = GalleryImage.objects.all()
    if category_filter:
        images = images.filter(category=category_filter)

    academy = get_academy_info()
    context = {
        'page_title': 'गॅलरी | Gallery',
        'meta_desc': 'Photo gallery of Sangharsh Career Academy Fulambri',
        'images': images,
        'active_cat': category_filter,
        'categories': GalleryImage.CATEGORY_CHOICES,
        'academy': academy,
    }
    return render(request, 'core/gallery.html', context)


def facilities(request):
    academy = get_academy_info()
    context = {
        'page_title': 'सुविधा | Facilities & Infrastructure',
        'meta_desc': 'World-class facilities at Sangharsh Career Academy Fulambri',
        'academy': academy,
    }
    return render(request, 'core/facilities.html', context)


def contact(request):
    academy = get_academy_info()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        msg = request.POST.get('message', '').strip()

        if name and mobile and msg:
            ContactMessage.objects.create(
                name=name, mobile=mobile, email=email, message=msg
            )
            messages.success(request, '✅ तुमचा संदेश मिळाला! आम्ही लवकरच संपर्क करू.')
            return redirect('contact')
        else:
            messages.error(request, '❌ कृपया सर्व आवश्यक माहिती भरा.')

    context = {
        'page_title': 'संपर्क | Contact Us',
        'meta_desc': 'Contact Sangharsh Career Academy Fulambri for admissions',
        'academy': academy,
    }
    return render(request, 'core/contact.html', context)
