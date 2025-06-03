from django import forms


class UploadFileForm(forms.Form):
    author = forms.CharField(label="Ф.И. ученика")
    file = forms.FileField(label="Файл")