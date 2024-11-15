import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'Optimal_Performance_Platform.settings'  # Ensure this matches your project structure
django.setup()
