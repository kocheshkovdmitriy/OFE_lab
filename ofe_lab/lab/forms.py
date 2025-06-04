from email.policy import default

from django import forms


class UploadFileForm(forms.Form):
    author = forms.CharField(label="Ф.И. ученика")
    file = forms.FileField(label="Файл")


class AuthUser(forms.Form):
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)