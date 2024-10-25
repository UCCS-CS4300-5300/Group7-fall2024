from django.core.management.base import BaseCommand
from home.models import Build

class Command(BaseCommand):
    help = 'Clear all builds from the database'

    def handle(self, *args, **kwargs):
        Build.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all builds'))
