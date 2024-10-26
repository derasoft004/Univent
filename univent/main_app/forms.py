from django import forms


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

