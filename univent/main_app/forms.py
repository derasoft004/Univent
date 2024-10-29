from django import forms
from django.forms import DateInput, TimeInput, DateTimeInput


class LoginUserForm(forms.Form):
    nickname = forms.CharField(max_length=255, label="Имя пользователя", widget=forms.TextInput)
    password = forms.CharField(max_length=255, label="Пароль", widget=forms.PasswordInput)


class RegisterUserForm(forms.Form):
    name = forms.CharField(max_length=255, label="Введите ваше имя", widget=forms.TextInput, required=False)
    surname = forms.CharField(max_length=255, label="Введите вашу фамилию", widget=forms.TextInput, required=False)
    age = forms.IntegerField(label="Сколько вам лет", widget=forms.TextInput, required=False)
    hobby = forms.CharField(label="Какие у вас хобби", widget=forms.TextInput, required=False)
    nickname = forms.CharField(max_length=255, label="Имя пользователя", widget=forms.TextInput)
    password = forms.CharField(max_length=255, label="Пароль", widget=forms.PasswordInput)


class RegisterPosterForm(forms.Form):
    title = forms.CharField(max_length=255, label="Введите название мероприятия", widget=forms.TextInput,
                            required=False)
    place = forms.CharField(max_length=255, label="Выберите место проведения", widget=forms.TextInput, required=False)
    price = forms.IntegerField(label="Цена входа", widget=forms.TextInput, required=False)
    short_description = forms.CharField(label="Краткое описание", widget=forms.TextInput, required=False)
    full_description = forms.CharField(max_length=1023, label="Подробное описание", widget=forms.TextInput)
    time_event = forms.DateTimeField(label="Дата и время проведения", widget=forms.DateTimeInput)


class SignForPoster(forms.Form):
    comment = forms.CharField(max_length=255, label="Описание к заявке", widget=forms.TextInput,
                              required=False)
    datetime_field = forms.DateTimeField(label="Удобное время для связи", widget=DateTimeInput(attrs={'type': 'datetime-local'}))
