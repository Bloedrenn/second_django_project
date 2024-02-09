from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )

    password_confirmation = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput
    )

    def clean_password_confirmation(self):
        if self.cleaned_data['password_confirmation'] != self.cleaned_data['password']:
            raise forms.ValidationError('Пароли не совпадают')
        
        return self.cleaned_data['password_confirmation']

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email'] # '__all__' если хотим использовать все атрибуты

        help_texts = {
            'username': 'Допускаются буквы, цифры и символы: @/./+/-/_'
        }

        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта'
        }
