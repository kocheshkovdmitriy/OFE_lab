from django.core.management.base import BaseCommand
from openpyxl import load_workbook
from lab import models

class Command(BaseCommand):
    help = '''Очищение базы данных учеников и протоколов. Удаляет полностью всех учеников и сданные ими протоколы'''

    def handle(self, *args, **options):
        print('Run custom command!')
        students = self.__get_students()
        for student in students:
            print('удаление студента:', student)
            student.delete()


    def __get_students(self):
        return models.Student.objects.all()

