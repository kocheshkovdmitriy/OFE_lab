from email.policy import default

from django import forms
from lab import models


class UploadFileForm(forms.Form):
    grade = forms.ChoiceField(choices=tuple((g.id, g.name) for g in models.Grade.objects.all()), required=False, label='Класс')
    litter = forms.ChoiceField(choices=tuple((lit.id, lit.name) for lit in models.Litter.objects.all()), required=False, label='Литер')
    students =  forms.ChoiceField(choices=tuple((st.id, st) for st in models.Student.objects.all()), required=False, label='Ученик')
    file = forms.FileField(label="Файл")


class AuthUser(forms.Form):
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)