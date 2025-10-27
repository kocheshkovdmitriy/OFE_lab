from django.core.management.base import BaseCommand
from openpyxl import load_workbook
from lab import models

class Command(BaseCommand):
    help = 'Fill in the database with students'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='Имя файла со списком учеников класса')
        parser.add_argument('class', type=int, help='Номер класса')
        parser.add_argument('litter', type=str, help='Литер класса')
    def handle(self, *args, **options):
        print('Run custom command!')
        grade = self.__get_class(options['class'])
        litter = self.__get_litter(options['litter'])

        if not (grade and litter):
            print('Не найден класс или литер в базе данных')
            print(grade, litter)
        else:
            wb = load_workbook(filename='temp/' + options['file_name'])

            students = []
            for cell in wb['Лист1']:
                print([i.value for i in cell])
                students.append(models.Student(
                    grade=grade,
                    label=litter,
                    first_name=cell[2].value,
                    second_name=cell[3].value,
                    last_name=cell[1].value
                ))
            models.Student.objects.bulk_create(students)

    def __get_class(self, grade: int):
        return models.Grade.objects.filter(name=grade).first()

    def __get_litter(self, litter: str):
        return models.Litter.objects.filter(name=litter).first()