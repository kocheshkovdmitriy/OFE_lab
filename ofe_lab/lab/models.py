from django.db import models


class Work(models.Model):
    grade = models.IntegerField(verbose_name='класс', blank=True)
    number = models.IntegerField(verbose_name='номер', blank=True)
    name = models.CharField(verbose_name='название', max_length=240, blank=True)
    url = models.CharField(verbose_name='url', max_length=240, blank=True)

    def __str__(self):
        return f'{self.grade} {self.number} {self.name}'

    class Meta:
        verbose_name = 'Лабораторная работа'
        verbose_name_plural = 'Лабораторные работы'
