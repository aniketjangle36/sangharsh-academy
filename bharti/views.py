from django.shortcuts import render
from .models import Bharti
from core.models import AcademyInfo


def bharti_list(request):
    category = request.GET.get('cat', 'all')
    bhartis = Bharti.objects.filter(is_active=True)

    if category == 'army':
        bhartis = bhartis.filter(category='army')
    elif category == 'police':
        bhartis = bhartis.filter(category='police')
    elif category == 'maha_police':
        bhartis = bhartis.filter(category='maha_police')

    academy = AcademyInfo.get_info()
    context = {
        'page_title': 'नवीनतम भरती | Latest Bharti Updates',
        'meta_desc': 'Latest Army and Police recruitment notifications 2026',
        'bhartis': bhartis,
        'active_cat': category,
        'academy': academy,
    }
    return render(request, 'bharti/bharti_list.html', context)
