from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poster/', views.poster, name='poster'),
    path('personal_account/', views.personal_account, name='personal_account'),
]
