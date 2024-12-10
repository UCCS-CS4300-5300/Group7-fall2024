# scripts/create_attributes.py
import os
import sys
import django
from home.models import CPUSocketType, FormFactor, StorageType, StorageCapacity, Microarchitecture

print("Starting create_attributes.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


# Create CPU Socket Types
cpu_sockets = ['LGA1151', 'AM4', 'AM5', 'LGA1700', 'LGA1200', 'LGA2066', 'TRX40', 'sTRX4', 'sWRX8']
for socket in cpu_sockets:
    CPUSocketType.objects.get_or_create(name=socket)

# Create Form Factors
form_factors = ['ATX', 'Micro-ATX', 'Mini-ITX', 'E-ATX', 'M.2', '2.5"', '3.5"', 'XL-ATX', 'Nano-ITX', 'Pico-ITX']
for form_factor in form_factors:
    FormFactor.objects.get_or_create(name=form_factor)

# Create Storage Types
storage_types = ['SSD', 'HDD', 'NVMe', 'SATA', 'M.2', 'U.2']
for storage_type in storage_types:
    StorageType.objects.get_or_create(type=storage_type)

# Create Storage Capacities
storage_capacities = ['128GB', '256GB', '512GB', '500GB', '960GB', '1TB', '2TB', '4TB', '8TB', '16TB', '32TB']
for capacity in storage_capacities:
    StorageCapacity.objects.get_or_create(capacity=capacity)

# Create Microarchitectures
microarchitectures = [
    'Skylake', 'Zen 3', 'Kaby Lake', 'Zen 2', 'Comet Lake',
    'Alder Lake', 'Rocket Lake', 'Zen', 'Coffee Lake', 'Ice Lake', 'Tiger Lake', 'Cascade Lake'
    ]
for microarchitecture in microarchitectures:
    Microarchitecture.objects.get_or_create(name=microarchitecture)

print("Attributes created successfully.")

# Print Results
print('CPU Socket Types:', ', '.join(cpu_sockets))
print('Form Factors:', ', '.join(form_factors))
print('Storage Types:', ', '.join(storage_types))
print('Storage Capacities:', ', '.join(storage_capacities))
print('Microarchitectures:', ', '.join(microarchitectures))

print("Completed create_attributes.py script.")
