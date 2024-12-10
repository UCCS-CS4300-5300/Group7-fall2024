# scripts/create_storages.py
import os
import sys
import django

print("Starting create_storages.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

print("Django setup completed.")

from home.models import Storage, Manufacturer, FormFactor, StorageType, StorageCapacity

print("Models imported successfully.")

# Verify Manufacturers
manufacturers = ['Samsung', 'Western Digital', 'Crucial', 'Seagate', 'Kingston', 'Intel', 'Toshiba']
for manufacturer in manufacturers:
    Manufacturer.objects.get_or_create(name=manufacturer)

# Verify Form Factors
form_factors = ['M.2', '2.5"', '3.5"', 'U.2']
for form_factor in form_factors:
    FormFactor.objects.get_or_create(name=form_factor)

# Verify Storage Types
storage_types = ['SSD', 'HDD', 'NVMe', 'SATA', 'M.2', 'U.2']
for storage_type in storage_types:
    StorageType.objects.get_or_create(type=storage_type)

# Verify Storage Capacities
storage_capacities = ['128GB', '256GB', '512GB', '1TB', '2TB', '4TB', '8TB', '16TB', '32TB']
for capacity in storage_capacities:
    StorageCapacity.objects.get_or_create(capacity=capacity)

# Create Storages
storages = [
    {
        'name': 'Samsung 970 EVO',
        'manufacturer': 'Samsung',
        'form_factor': 'M.2',
        'capacity': '1TB',
        'type': 'SSD',
        'price': 150
    },
    {
        'name': 'Western Digital Blue',
        'manufacturer': 'Western Digital',
        'form_factor': '2.5"',
        'capacity': '500GB',
        'type': 'HDD',
        'price': 50
    },
    {
        'name': 'Crucial MX500',
        'manufacturer': 'Crucial',
        'form_factor': '2.5"',
        'capacity': '1TB',
        'type': 'SSD',
        'price': 110
    },
    {
        'name': 'Seagate Barracuda',
        'manufacturer': 'Seagate',
        'form_factor': '3.5"',
        'capacity': '2TB',
        'type': 'HDD',
        'price': 60
    },
    {
        'name': 'Kingston A2000',
        'manufacturer': 'Kingston',
        'form_factor': 'M.2',
        'capacity': '512GB',
        'type': 'NVMe',
        'price': 80
    },
    {
        'name': 'Intel Optane 905P',
        'manufacturer': 'Intel',
        'form_factor': 'U.2',
        'capacity': '960GB',
        'type': 'NVMe',
        'price': 600
    },
    {
        'name': 'Toshiba X300',
        'manufacturer': 'Toshiba',
        'form_factor': '3.5"',
        'capacity': '4TB',
        'type': 'HDD',
        'price': 120
    },
    {
        'name': 'Samsung 860 EVO',
        'manufacturer': 'Samsung',
        'form_factor': '2.5"',
        'capacity': '1TB',
        'type': 'SATA',
        'price': 100
    },
    {
        'name': 'Crucial P1',
        'manufacturer': 'Crucial',
        'form_factor': 'M.2',
        'capacity': '1TB',
        'type': 'NVMe',
        'price': 110
    },
    {
        'name': 'Seagate IronWolf',
        'manufacturer': 'Seagate',
        'form_factor': '3.5"',
        'capacity': '8TB',
        'type': 'HDD',
        'price': 250
    }
]

print("Creating Storages...")

for storage_data in storages:
    try:
        manufacturer = Manufacturer.objects.get(name=storage_data['manufacturer'])
        form_factor = FormFactor.objects.get(name=storage_data['form_factor'])
        storage_type = StorageType.objects.get(type=storage_data['type'])
        capacity = StorageCapacity.objects.get(capacity=storage_data['capacity'])

        print(f"Manufacturer found: {manufacturer}")
        print(f"Form Factor found: {form_factor}")
        print(f"Storage Type found: {storage_type}")
        print(f"Capacity found: {capacity}")

        storage, created = Storage.objects.get_or_create(
            name=storage_data['name'],
            manufacturer=manufacturer,
            form_factor=form_factor,
            type=storage_type,
            capacity=capacity,
            defaults={'price': storage_data['price']}
        )
        if created:
            print(f"Storage {storage_data['name']} created.")
        else:
            print(f"Storage {storage_data['name']} already exists.")
    except Exception as e:
        print(f"Error creating storage {storage_data['name']}: {e}")

print("Completed create_storages.py script.")
