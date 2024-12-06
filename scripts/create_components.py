# scripts/create_components.py
import os
import sys
import django

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

from home.models import Manufacturer, CPUSocketType, FormFactor, Motherboard, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, RAM, Microarchitecture, CPU, Storage, StorageType, StorageCapacity

# Create Manufacturers (if not already created)
manufacturer_asus, created = Manufacturer.objects.get_or_create(name='ASUS')
manufacturer_intel, created = Manufacturer.objects.get_or_create(name='Intel')
manufacturer_kingston, created = Manufacturer.objects.get_or_create(name='Kingston')
manufacturer_samsung, created = Manufacturer.objects.get_or_create(name='Samsung')
manufacturer_wd, created = Manufacturer.objects.get_or_create(name='Western Digital')
manufacturer_amd, created = Manufacturer.objects.get_or_create(name='AMD')

# Create Motherboards
form_factor_atx = FormFactor.objects.get(name='ATX')
form_factor_micro_atx = FormFactor.objects.get(name='Micro-ATX')
cpu_socket_lga1151 = CPUSocketType.objects.get(name='LGA1151')
cpu_socket_am4 = CPUSocketType.objects.get(name='AM4')

motherboard_asus_rog, created = Motherboard.objects.get_or_create(
    name='ASUS ROG Strix',
    manufacturer=manufacturer_asus,
    cpu_socket_type=cpu_socket_lga1151,
    memory_slots=4,
    form_factor=form_factor_atx,
    max_memory_capacity=64,
    price=200,
    description='High performance motherboard with RGB lighting.'
)

motherboard_asus_prime, created = Motherboard.objects.get_or_create(
    name='ASUS Prime B450M-A',
    manufacturer=manufacturer_asus,
    cpu_socket_type=cpu_socket_am4,
    memory_slots=2,
    form_factor=form_factor_micro_atx,
    max_memory_capacity=32,
    price=100,
    description='Affordable motherboard with essential features.'
)

# Create RAM
ram_kingston_16gb, created = RAM.objects.get_or_create(
    name='Kingston HyperX Fury 16GB',
    manufacturer=manufacturer_kingston,
    ram_type=RAMType.objects.get(type='DDR4'),
    ram_speed=RAMSpeed.objects.get(speed=3200),
    ram_capacity=RAMCapacity.objects.get(capacity='16GB'),
    ram_number_of_modules=RAMNumberOfModules.objects.get(number_of_modules=2),
    price=80,
    description='High performance RAM for gaming and multitasking.'
)

ram_kingston_8gb, created = RAM.objects.get_or_create(
    name='Kingston HyperX Fury 8GB',
    manufacturer=manufacturer_kingston,
    ram_type=RAMType.objects.get(type='DDR3'),
    ram_speed=RAMSpeed.objects.get(speed=2400),
    ram_capacity=RAMCapacity.objects.get(capacity='8GB'),
    ram_number_of_modules=RAMNumberOfModules.objects.get(number_of_modules=4),
    price=40,
    description='Affordable RAM for basic computing needs.'
)

# Additional RAM instances
ram_corsair_16gb, created = RAM.objects.get_or_create(
    name='Corsair Vengeance LPX 16GB',
    manufacturer=Manufacturer.objects.get(name='Corsair'),
    ram_type=RAMType.objects.get(type='DDR4'),
    ram_speed=RAMSpeed.objects.get(speed=3000),
    ram_capacity=RAMCapacity.objects.get(capacity='16GB'),
    ram_number_of_modules=RAMNumberOfModules.objects.get(number_of_modules=2),
    price=85,
    description='Reliable high-speed RAM.'
)

ram_gskill_32gb, created = RAM.objects.get_or_create(
    name='G.Skill Ripjaws V 32GB',
    manufacturer=Manufacturer.objects.get(name='G.Skill'),
    ram_type=RAMType.objects.get(type='DDR4'),
    ram_speed=RAMSpeed.objects.get(speed=3600),
    ram_capacity=RAMCapacity.objects.get(capacity='32GB'),
    ram_number_of_modules=RAMNumberOfModules.objects.get(number_of_modules=4),
    price=180,
    description='High performance RAM for multitasking.'
)

# Create Microarchitectures
microarchitecture_coffee_lake, created = Microarchitecture.objects.get_or_create(name='Coffee Lake')
microarchitecture_zen, created = Microarchitecture.objects.get_or_create(name='Zen')

# Create CPUs
cpu_i7_8700k, created = CPU.objects.get_or_create(
    name='Intel Core i7-8700K',
    manufacturer=manufacturer_intel,
    microarchitecture=microarchitecture_coffee_lake,
    socket_type=cpu_socket_lga1151,
    price=300,
    description='High performance CPU for gaming and productivity.'
)

cpu_ryzen_5_3600, created = CPU.objects.get_or_create(
    name='AMD Ryzen 5 3600',
    manufacturer=manufacturer_amd,
    microarchitecture=microarchitecture_zen,
    socket_type=cpu_socket_am4,
    price=200,
    description='Affordable CPU with excellent multitasking capabilities.'
)

# Additional CPU instances
cpu_i5_9600k, created = CPU.objects.get_or_create(
    name='Intel Core i5-9600K',
    manufacturer=manufacturer_intel,
    microarchitecture=microarchitecture_coffee_lake,
    socket_type=cpu_socket_lga1151,
    price=250,
    description='Great CPU for mid-range gaming and productivity.'
)

cpu_ryzen_7_3700x, created = CPU.objects.get_or_create(
    name='AMD Ryzen 7 3700X',
    manufacturer=manufacturer_amd,
    microarchitecture=microarchitecture_zen,
    socket_type=cpu_socket_am4,
    price=330,
    description='High-end CPU for multitasking and gaming.'
)

# Create Storages
storage_samsung_970, created = Storage.objects.get_or_create(
    name='Samsung 970 EVO',
    manufacturer=manufacturer_samsung,
    form_factor=FormFactor.objects.get(name='M.2'),
    capacity=StorageCapacity.objects.get(capacity='1TB'),
    type=StorageType.objects.get(type='SSD'),
    price=150,
    description='High performance NVMe SSD.'
)

storage_wd_blue, created = Storage.objects.get_or_create(
    name='Western Digital Blue',
    manufacturer=manufacturer_wd,
    form_factor=FormFactor.objects.get(name='2.5"'),
    capacity=StorageCapacity.objects.get(capacity='500GB'),
    type=StorageType.objects.get(type='HDD'),
    price=50,
    description='Reliable HDD for everyday use.'
)

# Additional Storage instances
storage_crucial_mx500, created = Storage.objects.get_or_create(
    name='Crucial MX500',
    manufacturer=Manufacturer.objects.get(name='Crucial'),
    form_factor=FormFactor.objects.get(name='2.5"'),
    capacity=StorageCapacity.objects.get(capacity='1TB'),
    type=StorageType.objects.get(type='SSD'),
    price=110,
    description='High performance SSD.'
)

storage_seagate_barracuda, created = Storage.objects.get_or_create(
    name='Seagate Barracuda',
    manufacturer=Manufacturer.objects.get(name='Seagate'),
    form_factor=FormFactor.objects.get(name='3.5"'),
    capacity=StorageCapacity.objects.get(capacity='2TB'),
    type=StorageType.objects.get(type='HDD'),
    price=60,
    description='High capacity HDD for extensive storage needs.'
)

# Print Results
print('Motherboards:', motherboard_asus_rog, motherboard_asus_prime)
print('RAM:', ram_kingston_16gb, ram_kingston_8gb, ram_corsair_16gb, ram_gskill_32gb)
print('CPUs:', cpu_i7_8700k, cpu_ryzen_5_3600, cpu_i5_9600k, cpu_ryzen_7_3700x)
print('Storages:', storage_samsung_970, storage_wd_blue, storage_crucial_mx500, storage_seagate_barracuda)
