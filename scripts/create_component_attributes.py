# scripts/create_component_attributes.py
import os
import sys
import django

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

from home.models import CPUSocketType, FormFactor, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, StorageType, StorageCapacity

# Create CPU Socket Types
cpu_socket_lga1151, created = CPUSocketType.objects.get_or_create(name='LGA1151')
cpu_socket_am4, created = CPUSocketType.objects.get_or_create(name='AM4')

# Create Form Factors
form_factor_atx, created = FormFactor.objects.get_or_create(name='ATX')
form_factor_micro_atx, created = FormFactor.objects.get_or_create(name='Micro-ATX')
form_factor_m2, created = FormFactor.objects.get_or_create(name='M.2')
form_factor_2_5, created = FormFactor.objects.get_or_create(name='2.5"')
form_factor_3_5, created = FormFactor.objects.get_or_create(name='3.5"')  # Add missing form factor

# Create RAM Types
ram_type_ddr4, created = RAMType.objects.get_or_create(type='DDR4')
ram_type_ddr3, created = RAMType.objects.get_or_create(type='DDR3')

# Create RAM Speeds
ram_speed_3200, created = RAMSpeed.objects.get_or_create(speed=3200)
ram_speed_2400, created = RAMSpeed.objects.get_or_create(speed=2400)
ram_speed_3000, created = RAMSpeed.objects.get_or_create(speed=3000)  # Ensure missing speed is added
ram_speed_3600, created = RAMSpeed.objects.get_or_create(speed=3600)

# Create RAM Capacities
ram_capacity_16gb, created = RAMCapacity.objects.get_or_create(capacity='16GB')
ram_capacity_8gb, created = RAMCapacity.objects.get_or_create(capacity='8GB')
ram_capacity_32gb, created = RAMCapacity.objects.get_or_create(capacity='32GB')

# Create RAM Number of Modules
ram_modules_2, created = RAMNumberOfModules.objects.get_or_create(number_of_modules=2)
ram_modules_4, created = RAMNumberOfModules.objects.get_or_create(number_of_modules=4)

# Create Storage Types
storage_type_ssd, created = StorageType.objects.get_or_create(type='SSD')
storage_type_hdd, created = StorageType.objects.get_or_create(type='HDD')

# Create Storage Capacities
capacity_1tb, created = StorageCapacity.objects.get_or_create(capacity='1TB')
capacity_500gb, created = StorageCapacity.objects.get_or_create(capacity='500GB')
capacity_2tb, created = StorageCapacity.objects.get_or_create(capacity='2TB')

# Print Results
print('CPU Socket Types:', cpu_socket_lga1151, cpu_socket_am4)
print('Form Factors:', form_factor_atx, form_factor_micro_atx, form_factor_m2, form_factor_2_5, form_factor_3_5)
print('RAM Types:', ram_type_ddr4, ram_type_ddr3)
print('RAM Speeds:', ram_speed_3200, ram_speed_2400, ram_speed_3000, ram_speed_3600)
print('RAM Capacities:', ram_capacity_16gb, ram_capacity_8gb, ram_capacity_32gb)
print('RAM Modules:', ram_modules_2, ram_modules_4)
print('Storage Types:', storage_type_ssd, storage_type_hdd)
print('Storage Capacities:', capacity_1tb, capacity_500gb, capacity_2tb)
