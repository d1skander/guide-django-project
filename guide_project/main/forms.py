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


class ReviewForm(forms.Form):
    from .models import verification_number_reviews
    text = forms.CharField(label="Текст", help_text="Посетили это место? Расскажите о своих впечатлениях!", widget=forms.Textarea)
    grade = forms.IntegerField(label="Оценка", help_text="Оцените это место от 1 до 5!", validators=[verification_number_reviews])


#эту часть снизу я дал ИИ(gemini)

# 1. Форма смены логина
class EditUsernameForm(forms.Form):
    username = forms.CharField(
        label="Новый логин", 
        max_length=20, 
        min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Новый логин'})
    )

# 2. Форма смены почты
class EditEmailForm(forms.Form):
    email = forms.EmailField(
        label="Новая почта",
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Новый email'})
    )

# 3. Форма смены пароля
class EditPasswordForm(forms.Form):
    password = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Новый пароль'})
    )
