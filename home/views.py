from django.shortcuts import render
from django.utils import timezone


def home(request):
    context = {
        'title': 'New Project',
        'subtitle': 'Content Title',
        'year': timezone.now().year,
    }
    return render(request, 'home.html', context)