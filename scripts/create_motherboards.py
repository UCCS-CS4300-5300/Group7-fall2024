# scripts/create_motherboards.py
import os
import sys
import django
from home.models import (
    Motherboard, CPUSocketType, FormFactor, Manufacturer,
    RAMType, RAMSpeed, SupportedRAMConfiguration
)

print("Starting create_motherboards.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


# Verify Manufacturers
manufacturers = ['ASUS', 'Gigabyte', 'MSI', 'ASRock', 'EVGA', 'Biostar']
for manufacturer in manufacturers:
    Manufacturer.objects.get_or_create(name=manufacturer)

# Verify CPU Socket Types
cpu_sockets = ['LGA1151', 'AM4', 'AM5', 'LGA1700', 'LGA1200', 'TRX40', 'sTRX4', 'LGA3647', 'sWRX8']
for socket in cpu_sockets:
    CPUSocketType.objects.get_or_create(name=socket)

# Verify Form Factors
form_factors = ['ATX', 'Micro-ATX', 'Mini-ITX', 'E-ATX', 'XL-ATX', 'Nano-ITX', 'Pico-ITX']
for form_factor in form_factors:
    FormFactor.objects.get_or_create(name=form_factor)

# Verify RAM Types
ram_types = ['DDR4', 'DDR3', 'DDR5']
for ram_type in ram_types:
    RAMType.objects.get_or_create(type=ram_type)

# Verify RAM Speeds
ram_speeds = [2133, 2400, 2666, 3000, 3200, 3600, 4000, 4400, 4800, 5200, 5600, 6000]
for ram_speed in ram_speeds:
    RAMSpeed.objects.get_or_create(speed=ram_speed)

# Create Motherboards
motherboards = [
    {
        'name': 'ASUS ROG Strix',
        'manufacturer': 'ASUS',
        'cpu_socket_type': 'LGA1151',
        'memory_slots': 4,
        'form_factor': 'ATX',
        'max_memory_capacity': 64,
        'price': 200,
        'description': 'High performance motherboard with RGB lighting.',
        'supported_ram_types': ['DDR4'],
        'supported_ram_speeds': [3200]
    },
    {
        'name': 'ASUS ROG Zenith II Extreme Alpha',
        'manufacturer': 'ASUS',
        'cpu_socket_type': 'sTRX4',
        'memory_slots': 8,
        'form_factor': 'E-ATX',
        'max_memory_capacity': 256,
        'price': 700,
        'description': 'High-end motherboard supporting latest Ryzen Threadripper processors and DDR4 memory.',
        'supported_ram_types': ['DDR4'],
        'supported_ram_speeds': [3200, 3600]
    },
    {
        'name': 'Gigabyte Z690 AORUS MASTER',
        'manufacturer': 'Gigabyte',
        'cpu_socket_type': 'LGA1700',
        'memory_slots': 4,
        'form_factor': 'ATX',
        'max_memory_capacity': 128,
        'price': 400,
        'description': 'High-end motherboard for Intel 12th Gen processors with DDR5 support.',
        'supported_ram_types': ['DDR5', 'DDR4'],
        'supported_ram_speeds': [4800, 5200]
    },
    {
        'name': 'ASUS Prime B450M-A',
        'manufacturer': 'ASUS',
        'cpu_socket_type': 'AM4',
        'memory_slots': 2,
        'form_factor': 'Micro-ATX',
        'max_memory_capacity': 32,
        'price': 100,
        'description': 'Affordable motherboard with essential features.',
        'supported_ram_types': ['DDR4'],
        'supported_ram_speeds': [2400]
    },
    {
        'name': 'ASRock X570 Taichi',
        'manufacturer': 'ASRock',
        'cpu_socket_type': 'AM4',
        'memory_slots': 4,
        'form_factor': 'ATX',
        'max_memory_capacity': 128,
        'price': 300,
        'description': 'High-end motherboard with PCIe 4.0 support and robust power delivery.',
        'supported_ram_types': ['DDR4'],
        'supported_ram_speeds': [3200, 3600]
    }
]

print("\nAttempting to create motherboards...\n")
for mb_data in motherboards:
    manufacturer = Manufacturer.objects.get(name=mb_data['manufacturer'])
    cpu_socket = CPUSocketType.objects.get(name=mb_data['cpu_socket_type'])
    form_factor = FormFactor.objects.get(name=mb_data['form_factor'])

    motherboard, created = Motherboard.objects.get_or_create(
        name=mb_data['name'],
        manufacturer=manufacturer,
        cpu_socket_type=cpu_socket,
        max_memory_capacity=mb_data['max_memory_capacity'],
        memory_slots=mb_data['memory_slots'],
        form_factor=form_factor,
        price=mb_data['price'],
        description=mb_data['description']
    )

    if created:
        for ram_type in mb_data['supported_ram_types']:
            ram_type_obj = RAMType.objects.get(type=ram_type)
            supported_speeds = ','.join(str(speed) for speed in mb_data['supported_ram_speeds'])
            SupportedRAMConfiguration.objects.create(
                motherboard=motherboard,
                ram_type=ram_type_obj,
                supported_speeds=supported_speeds  # Comma-separated values of supported speeds
            )

        motherboard.save()
        print(f"Motherboard {mb_data['name']} created and RAM configurations associated.")
    else:
        print(f"Motherboard {mb_data['name']} already exists.")

print("\nCompleted create_motherboards.py script.")
