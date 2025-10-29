from django.contrib import admin

from lab import models


@admin.register(models.Grade)
class Grade(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Letter)
class Letter(admin.ModelAdmin):
    list_display = ['name']
@admin.register(models.Protocol)
class Protocols(admin.ModelAdmin):
    list_display = ['work', 'author', 'file', 'time_create', 'accepted']


@admin.register(models.Work)
class Work(admin.ModelAdmin):
    list_display = ['grade', 'number', 'name', 'url']


@admin.register(models.Student)
class Student(admin.ModelAdmin):
    list_display = ['full_name', 'get_grade']

    def full_name(self, object):
        return f'{object.first_name} {object.last_name}'

    def get_grade(self, object):
        return f'{object.grade.name}{object.label}'

    full_name.short_description = 'Имя Фамилия'
    get_grade.short_description = 'Класс'
