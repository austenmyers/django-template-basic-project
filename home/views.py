from django.shortcuts import render


def home(request):
    context = {
        'welcome': 'Hello, World!'
    }
    return render(request, 'home.html', context)