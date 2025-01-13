from django.utils import timezone


context = {
    'title': 'New Project',
    'subtitle': 'Content Title',
    'year': timezone.now().year,
}