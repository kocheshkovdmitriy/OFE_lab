from email.policy import default

from django import forms
from lab import models


class ChoiceClass(forms.Form):
    grade = forms.ChoiceField(choices=tuple((g.id, g.name) for g in models.Grade.objects.all()), required=False, label='Класс')
    litter = forms.ChoiceField(choices=tuple((lit.id, lit.name) for lit in models.Litter.objects.all()), required=False, label='Литер')

class UploadFileForm(forms.Form):
    #CHOICES = tuple((st.id, st) for st in models.Student.objects.all())
    #students = forms.ChoiceField(choices= CHOICES, required=False, label='Ученик')
    file = forms.FileField(label="Файл")

    def __init__(self, *args, grade=None, lit=None, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['students'] = forms.ChoiceField(
            choices=self.get_choices(grade=grade, lit=lit),
            required=False,
            label='Ученик'
        )

    def get_choices(self, grade=None, lit=None):
        return tuple((st.id, st) for st in models.Student.objects.filter(grade_id=grade, label_id=lit))


class AuthUser(forms.Form):
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)