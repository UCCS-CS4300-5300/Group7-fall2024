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
manufacturers = ['ASUS', 'Intel', 'Kingston', 'Samsung', 'Western Digital', 'AMD', 'Corsair', 'G.Skill', 'Crucial', 'Seagate']
for manufacturer in manufacturers:
    Manufacturer.objects.get_or_create(name=manufacturer)

# Print Results
print('Manufacturers:', ', '.join(manufacturers))
