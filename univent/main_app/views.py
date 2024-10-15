from django.shortcuts import render

def index(request):
    data = {'var': 15}
    return render(request, 'index.html', context=data)

def poster(request):
    data: dict = {'posters': dict((f'event_{n}', round(n * 3 + 50 / n)) for n in range(1, 11))}
    return render(request, 'poster.html', context=data)


