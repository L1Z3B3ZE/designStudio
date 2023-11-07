import re
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ('name', 'username', 'email', 'password1', 'password2', 'is_activated')

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[а-яА-Я\s-]+$', name):
            raise ValidationError("ФИО может содержать только кириллицу, дефис и пробелы. ")
        return name

    def clean_login(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z\s-]+$', username):
            raise ValidationError("Логин может содержать только латиницу и дефис. ")
        if AdvUser.objects.filter(username=username).exists():
            raise ValidationError("Пользователь с таким логином уже существует. ")
        return username


class ChangeRequestStatusForm(forms.ModelForm):
    comment = forms.CharField(required=False)
    design = forms.ImageField(required=False)

    class Meta:
        model = Application
        fields = ['status', 'comment', 'design']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        comment = cleaned_data.get('comment')
        design = cleaned_data.get('design')

        if status == 'Принято в работу' and not comment:
            self.add_error('comment', 'Комментарий обязателен при смене статуса на "Принято в работу".')
        elif status == 'Выполнено' and not design:
            self.add_error('design', 'Дизайн обязателен при смене статуса на "Выполнено".')