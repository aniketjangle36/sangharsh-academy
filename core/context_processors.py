from .models import AcademyInfo


def global_context(request):
    """Make academy info available in all templates"""
    academy = AcademyInfo.get_info()
    return {
        'site_academy': academy,
        'whatsapp_number': academy.whatsapp.replace('+', '').replace(' ', ''),
    }
