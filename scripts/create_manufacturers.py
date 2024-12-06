# scripts/create_manufacturers.py
import os
import sys
import django

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

from home.models import Manufacturer

# Create Manufacturers
manufacturer_asus, created = Manufacturer.objects.get_or_create(name='ASUS')
manufacturer_intel, created = Manufacturer.objects.get_or_create(name='Intel')
manufacturer_kingston, created = Manufacturer.objects.get_or_create(name='Kingston')
manufacturer_samsung, created = Manufacturer.objects.get_or_create(name='Samsung')
manufacturer_wd, created = Manufacturer.objects.get_or_create(name='Western Digital')
manufacturer_amd, created = Manufacturer.objects.get_or_create(name='AMD')

# Add additional manufacturers
manufacturer_corsair, created = Manufacturer.objects.get_or_create(name='Corsair')
manufacturer_gskill, created = Manufacturer.objects.get_or_create(name='G.Skill')
manufacturer_crucial, created = Manufacturer.objects.get_or_create(name='Crucial')
manufacturer_seagate, created = Manufacturer.objects.get_or_create(name='Seagate')

# Print Results
print('Manufacturers:', manufacturer_asus, manufacturer_intel, manufacturer_kingston, manufacturer_samsung, manufacturer_wd, manufacturer_amd, manufacturer_corsair, manufacturer_gskill, manufacturer_crucial, manufacturer_seagate)
