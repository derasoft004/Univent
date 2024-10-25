from django.shortcuts import render

from .models import Poster

def index(request):
    data = {'var': 15}
    return render(request, 'index.html', context=data)

def poster(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'poster.html', context=data)


def personal_account(request):
    data = {}
    return render(request, 'personal_account.html', context=data)


