from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=200, verbose_name='раздел')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Раздел спавочника'
        verbose_name_plural = 'Разделы справочника'

class Article(models.Model):
    section = models.ForeignKey(Section, verbose_name='раздел', on_delete=models.CASCADE, related_name='articles')
    priority = models.IntegerField(verbose_name='приоритет')
    name = models.CharField(max_length=200, verbose_name='название')
    path_to_file = models.CharField(max_length=200, verbose_name='путь к файлу')

    def __str__(self):
        return f'Раздел {self.section.id}: {self.name}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
