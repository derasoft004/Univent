from django.shortcuts import render

def index(request):
    data = {'var': 15}
    return render(request, 'index.html', context=data)


