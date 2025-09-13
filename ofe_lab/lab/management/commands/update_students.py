from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fill in the database with students'

    def handle(self, *args, **options):
        import this