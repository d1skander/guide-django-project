from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=20, min_length=3, 
                               help_text="Используется для входа. Допускаются только латинские буквы и цифры.")
    email = forms.EmailField(label="Почта", min_length=3, 
                             help_text="Укажите email.")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput,
                               help_text="Придумайте надежный пароль. Не используйте простые комбинации.")


class AuthForm(forms.Form):
    username = forms.CharField(label="Логин", max_length=20, min_length=3, 
                               help_text="Введите логин для входа.")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, 
                               help_text="Введите пароль для входа.")