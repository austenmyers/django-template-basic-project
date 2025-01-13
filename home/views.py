from django.shortcuts import render
from tools import context


def home(request):

    return render(request, 'home.html', context)