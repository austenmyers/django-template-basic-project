from django.shortcuts import render
from utilities.context import get_context


def home(request):
    context = get_context()
    context['subtitle'] = 'Welcome'

    return render(request, 'home.html', context)