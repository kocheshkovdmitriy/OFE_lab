from django.contrib import admin

from lab import models


@admin.register(models.Decision)
class Decision(admin.ModelAdmin):
    list_display = ['work', 'author', 'file']


@admin.register(models.Work)
class Decision(admin.ModelAdmin):
    list_display = ['grade', 'number', 'name', 'url']
