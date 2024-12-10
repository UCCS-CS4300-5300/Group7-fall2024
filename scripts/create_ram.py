# scripts/create_ram.py
import os
import sys
import django
from home.models import RAM, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, Manufacturer

print("Starting create_ram.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

# Verify Manufacturers
manufacturers = ['Kingston', 'Corsair', 'G.Skill', 'Crucial', 'HyperX']
for manufacturer in manufacturers:
    Manufacturer.objects.get_or_create(name=manufacturer)

# Verify RAM Types
ram_types = ['DDR4', 'DDR3', 'DDR5']
for ram_type in ram_types:
    RAMType.objects.get_or_create(type=ram_type)

# Verify RAM Speeds
ram_speeds = [2133, 2400, 2666, 3000, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000]
for ram_speed in ram_speeds:
    RAMSpeed.objects.get_or_create(speed=ram_speed)

# Verify RAM Capacities
ram_capacities = ['4GB', '8GB', '16GB', '32GB', '64GB']
for ram_capacity in ram_capacities:
    RAMCapacity.objects.get_or_create(capacity=ram_capacity)

# Verify RAM Number of Modules
ram_modules = [1, 2, 4, 8]
for ram_module in ram_modules:
    RAMNumberOfModules.objects.get_or_create(number_of_modules=ram_module)

# Create RAM
rams = [
    {
        'name': 'Kingston HyperX Fury 16GB',
        'manufacturer': 'Kingston',
        'ram_type': 'DDR4',
        'ram_speed': 3200,
        'ram_capacity': '16GB',
        'ram_number_of_modules': 2,
        'price': 75
    },
    {
        'name': 'Kingston HyperX Fury 8GB',
        'manufacturer': 'Kingston',
        'ram_type': 'DDR3',
        'ram_speed': 2400,
        'ram_capacity': '8GB',
        'ram_number_of_modules': 4,
        'price': 50
    },
    {
        'name': 'Corsair Vengeance LPX 16GB',
        'manufacturer': 'Corsair',
        'ram_type': 'DDR4',
        'ram_speed': 3000,
        'ram_capacity': '16GB',
        'ram_number_of_modules': 2,
        'price': 80
    },
    {
        'name': 'G.Skill Ripjaws V 32GB',
        'manufacturer': 'G.Skill',
        'ram_type': 'DDR4',
        'ram_speed': 3600,
        'ram_capacity': '32GB',
        'ram_number_of_modules': 4,
        'price': 150
    },
    {
        'name': 'Crucial Ballistix 16GB',
        'manufacturer': 'Crucial',
        'ram_type': 'DDR4',
        'ram_speed': 3200,
        'ram_capacity': '16GB',
        'ram_number_of_modules': 2,
        'price': 70
    },
    {
        'name': 'Corsair Dominator Platinum 32GB',
        'manufacturer': 'Corsair',
        'ram_type': 'DDR5',
        'ram_speed': 5200,
        'ram_capacity': '32GB',
        'ram_number_of_modules': 2,
        'price': 250
    },
    {
        'name': 'G.Skill Trident Z RGB 64GB',
        'manufacturer': 'G.Skill',
        'ram_type': 'DDR4',
        'ram_speed': 4000,
        'ram_capacity': '64GB',
        'ram_number_of_modules': 4,
        'price': 300
    },
    {
        'name': 'HyperX Predator 16GB',
        'manufacturer': 'HyperX',
        'ram_type': 'DDR4',
        'ram_speed': 3600,
        'ram_capacity': '16GB',
        'ram_number_of_modules': 2,
        'price': 85
    }
]

print("Creating RAM...")

for ram_data in rams:
    try:
        manufacturer = Manufacturer.objects.get(name=ram_data['manufacturer'])
        ram_type = RAMType.objects.get(type=ram_data['ram_type'])
        ram_speed = RAMSpeed.objects.get(speed=ram_data['ram_speed'])
        ram_capacity = RAMCapacity.objects.get(capacity=ram_data['ram_capacity'])
        ram_number_of_modules = RAMNumberOfModules.objects.get(number_of_modules=ram_data['ram_number_of_modules'])

        print(f"Manufacturer found: {manufacturer}")
        print(f"RAM Type found: {ram_type}")
        print(f"RAM Speed found: {ram_speed}")
        print(f"RAM Capacity found: {ram_capacity}")
        print(f"RAM Number of Modules found: {ram_number_of_modules}")

        RAM.objects.get_or_create(
            name=ram_data['name'],
            manufacturer=manufacturer,
            ram_type=ram_type,
            ram_speed=ram_speed,
            ram_capacity=ram_capacity,
            ram_number_of_modules=ram_number_of_modules,
            defaults={'price': ram_data['price']}
        )
        print(f"RAM {ram_data['name']} created.")
    except Exception as e:
        print(f"Error creating RAM {ram_data['name']}: {e}")

print("Completed create_ram.py script.")
