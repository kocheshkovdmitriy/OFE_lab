from django.contrib import admin

from guide import models

@admin.register(models.Section)
class Section(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Article)
class Article(admin.ModelAdmin):
    list_display = ['section', 'name', 'path_to_file', 'priority']
