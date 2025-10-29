from email.policy import default

from django import forms
from lab import models


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл", required=False,)



class AuthUser(forms.Form):
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)