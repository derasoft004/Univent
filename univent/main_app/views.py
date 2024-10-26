from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import LoginUserForm, RegisterUserForm, RegisterPosterForm, SignForPoster
from .models import Poster, User


def index(request):
    data = {'posters': Poster.objects.all()}
    return render(request, 'index.html', context=data)


class Posters(ListView):
    # data = {'posters': Poster.objects.all()}
    # return render(request, 'posters.html', context=data)
    model = Poster
    template_name = 'posters.html'
    context_object_name = 'posters'
    paginate_by = 3
    extra_context = {
        'posters': Poster.objects.all(),
    }


def poster(request, post_slug):
    post = get_object_or_404(Poster, slug=post_slug)
    if request.method == 'POST':
        form = SignForPoster(request.POST)
        if form.is_valid():
            return redirect('personal_account')
    else:
        form = SignForPoster()
    context = {'post': post, 'form': form}
    return render(request, 'poster.html', context=context)


def personal_account(request):

    user_data = {}
    return render(request, 'personal_account.html', context=user_data)


def poster_redactor(request):
    if request.method == 'POST':
        form = RegisterPosterForm(request.POST)
        if form.is_valid():
            try:
                poster = Poster(title=form.cleaned_data['title'],
                                place=form.cleaned_data['place'],
                                price=form.cleaned_data['price'],
                                short_description=form.cleaned_data['short_description'],
                                full_description=form.cleaned_data['full_description'],
                                time_event=form.cleaned_data['time_event'])
                poster.save()
                return redirect('posters')
            except:
                form.add_error(None, 'Не удалось создать обьявление')
    else:
        form = RegisterPosterForm()
    data = {'form': form}
    return render(request, 'registration_page.html', context=data)


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
                rsp = redirect('index')
                rsp.set_cookie('nickname', form.cleaned_data['nickname'])
                return rsp
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
