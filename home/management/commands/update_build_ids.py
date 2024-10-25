from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Update build_id for records with null values'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE home_build SET build_id = (SELECT MAX(build_id) + 1 FROM home_build) WHERE build_id IS NULL")
        self.stdout.write(self.style.SUCCESS('Successfully updated build_id for records with null values'))
