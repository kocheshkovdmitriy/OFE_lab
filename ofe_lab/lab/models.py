from django.db import models

class Grade(models.Model):
    name = models.CharField(verbose_name='класс', max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

class Student(models.Model):
    grade = models.ForeignKey(Grade, verbose_name='класс', on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    second_name = models.CharField(verbose_name='Отчество', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)


class Work(models.Model):
    grade = models.ForeignKey(Grade, verbose_name='класс', on_delete=models.CASCADE, related_name='works')
    number = models.IntegerField(verbose_name='номер')
    name = models.CharField(verbose_name='название', max_length=240)
    url = models.CharField(verbose_name='url', max_length=240)

    def __str__(self):
        return f'{self.grade} {self.number} {self.name}'

    class Meta:
        verbose_name = 'Лабораторная работа'
        verbose_name_plural = 'Лабораторные работы'

class Protocol(models.Model):
    work = models.ForeignKey(Work, verbose_name='Лабораторная работа', on_delete=models.CASCADE, related_name='protocols')
    author = models.ForeignKey(Student, verbose_name='Ученик', on_delete=models.CASCADE, related_name='protocols')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Сдано')
    accepted = models.BooleanField(default=False, verbose_name='Подтверждение')

    def get_file_name(self):
        return self.file.name[8:]

    class Meta:
        verbose_name = 'Отчет по лабораторной работе'
        verbose_name_plural = 'Отчеты по лабораторной работе'
