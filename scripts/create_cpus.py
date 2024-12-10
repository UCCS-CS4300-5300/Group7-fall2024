# scripts/create_cpus.py
import os
import sys
import django

print("Starting create_cpus.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

print("Django setup completed.")

from home.models import CPU, Manufacturer, CPUSocketType, Microarchitecture

print("Models imported successfully.")

# Create CPUs
cpus = [
    {
        'name': 'Intel Core i7',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1151',
        'microarchitecture_name': 'Skylake',
        'price': 300
    },
    {
        'name': 'AMD Ryzen 9',
        'manufacturer_name': 'AMD',
        'socket_type_name': 'AM4',
        'microarchitecture_name': 'Zen 3',
        'price': 450
    },
    {
        'name': 'Intel Core i5',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1151',
        'microarchitecture_name': 'Kaby Lake',
        'price': 250
    },
    {
        'name': 'AMD Ryzen 5',
        'manufacturer_name': 'AMD',
        'socket_type_name': 'AM4',
        'microarchitecture_name': 'Zen 2',
        'price': 300
    },
    {
        'name': 'Intel Core i9',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1200',
        'microarchitecture_name': 'Comet Lake',
        'price': 500
    },
    {
        'name': 'AMD Ryzen 7',
        'manufacturer_name': 'AMD',
        'socket_type_name': 'AM4',
        'microarchitecture_name': 'Zen 3',
        'price': 400
    },
    {
        'name': 'Intel Core i3',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1151',
        'microarchitecture_name': 'Skylake',
        'price': 150
    },
    {
        'name': 'Intel Core i5 12600K',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1700',
        'microarchitecture_name': 'Alder Lake',
        'price': 320
    },
    {
        'name': 'AMD Ryzen 9 5950X',
        'manufacturer_name': 'AMD',
        'socket_type_name': 'AM4',
        'microarchitecture_name': 'Zen 3',
        'price': 799
    },
    {
        'name': 'Intel Core i7 12700K',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA1700',
        'microarchitecture_name': 'Alder Lake',
        'price': 420
    },
    {
        'name': 'Intel Xeon W-3275',
        'manufacturer_name': 'Intel',
        'socket_type_name': 'LGA3647',
        'microarchitecture_name': 'Cascade Lake',
        'price': 3000
    },
    {
        'name': 'AMD Threadripper 3990X',
        'manufacturer_name': 'AMD',
        'socket_type_name': 'sTRX4',
        'microarchitecture_name': 'Zen 2',
        'price': 4000
    }
]

print("Creating CPUs...")

for cpu_data in cpus:
    try:
        manufacturer = Manufacturer.objects.get(name=cpu_data['manufacturer_name'])
        socket_type = CPUSocketType.objects.get(name=cpu_data['socket_type_name'])
        microarchitecture = Microarchitecture.objects.get(name=cpu_data['microarchitecture_name'])

        print(f"Manufacturer found: {manufacturer}")
        print(f"CPU Socket Type found: {socket_type}")
        print(f"Microarchitecture found: {microarchitecture}")

        CPU.objects.get_or_create(
            name=cpu_data['name'],
            manufacturer=manufacturer,
            socket_type=socket_type,
            microarchitecture=microarchitecture,
            defaults={'price': cpu_data['price']}
        )
        print(f"CPU {cpu_data['name']} created.")
    except Exception as e:
        print(f"Error creating CPU {cpu_data['name']}: {e}")

print("Completed create_cpus.py script.")
