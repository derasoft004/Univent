from django.shortcuts import render, redirect
from base64 import b64encode, b64decode

from .forms import LoginUserForm
from .models import Poster, User


def index(request):
    data = {'var': 15}
    return render(request, 'index.html', context=data)


def poster(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'poster.html', context=data)


def personal_account(request):
    return render(request, 'personal_account.html')


def poster_redactor(request):
    data = {}
    return render(request, 'poster_redactor.html', context=data)


def registration_page(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            try:
                if User.objects.filter(nickname=form.cleaned_data['nickname']):
                    raise Exception
                user = User(nickname=form.cleaned_data['nickname'], password=form.cleaned_data['password'])
                user.save()
                return redirect('index')
            except:
                form.add_error(None, 'Пользователь с таким ником уже существует')
    else:
        form = LoginUserForm()
    data = {'form': form}
    return render(request, 'registration_page.html', context=data)

