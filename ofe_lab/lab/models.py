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

class Decision(models.Model):
    work = models.ForeignKey(Work, verbose_name='Лабораторная работа', on_delete=models.CASCADE, related_name='decisions')
    author = models.CharField(max_length=100, verbose_name='автор')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Сдано')

    def get_file_name(self):
        return self.file.name[8:]

    class Meta:
        verbose_name = 'Отчет по лабораторной работе'
        verbose_name_plural = 'Отчеты по лабораторной работе'
