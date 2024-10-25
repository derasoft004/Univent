from django import forms


class LoginUserForm(forms.Form):
    nickname = forms.CharField(max_length=255, label="Имя пользователя", widget=forms.TextInput)
    password = forms.CharField(max_length=255, label="Пароль", widget=forms.PasswordInput)
