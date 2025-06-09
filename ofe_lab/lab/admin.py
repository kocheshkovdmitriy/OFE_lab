from django.contrib import admin

from lab import models


@admin.register(models.Protocol)
class Protocols(admin.ModelAdmin):
    list_display = ['work', 'author', 'file', 'time_create', 'accepted']


@admin.register(models.Work)
class Work(admin.ModelAdmin):
    list_display = ['grade', 'number', 'name', 'url']


@admin.register(models.Student)
class Student(admin.ModelAdmin):
    list_display = ['grade', 'first_name', 'second_name', 'last_name']