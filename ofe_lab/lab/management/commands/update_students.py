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
        print(grade, litter)
        wb = load_workbook(filename='temp/' + options['file_name'])
        for cell in wb['Лист1']:
            if cell[0]:
                print(cell[1].value.split())

    def __get_class(self, grade: int):
        return models.Grade.objects.filter(name=grade)

    def __get_litter(self, litter: str):
        return models.Litter.objects.filter(name=litter)