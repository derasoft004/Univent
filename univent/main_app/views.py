from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginUserForm, RegisterUserForm
from .models import Poster, User


def index(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'index.html', context=data)


def posters(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'posters.html', context=data)


def poster(request, post_slug):
    post = get_object_or_404(Poster, slug=post_slug)
    context = {'post': post}
    return render(request, 'poster.html', context=context)


def personal_account(request):

    user_data = {}
    return render(request, 'personal_account.html', context=user_data)


def poster_redactor(request):
    data = {}
    return render(request, 'poster_redactor.html', context=data)


def registration_page(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            try:
                if User.objects.filter(nickname=form.cleaned_data['nickname']):
                    raise Exception
                user = User(nickname=form.cleaned_data['nickname'],
                            password=form.cleaned_data['password'],
                            name=form.cleaned_data['name'],
                            surname=form.cleaned_data['surname'],
                            age=form.cleaned_data['age'],
                            hobby=form.cleaned_data['hobby'])
                user.save()
                return redirect('index')
            except:
                form.add_error(None, 'Пользователь с таким ником уже существует')
    else:
        form = RegisterUserForm()
    data = {'form': form}
    return render(request, 'registration_page.html', context=data)


def login_page(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(nickname=form.cleaned_data['nickname']):
                return redirect('registration_page')
            elif User.objects.filter(nickname=form.cleaned_data['nickname'])[0].password != form.cleaned_data['password']:
                form.add_error(None, 'Неправильно указан пароль')
            else:
                return redirect('index')

    else:
        form = LoginUserForm()
    return render(request, 'login_page.html', context={'form': form})
