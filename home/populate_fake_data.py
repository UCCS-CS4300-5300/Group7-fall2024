import os
import sys
import django
import random
from faker import Faker

# Add project root to sys.path
sys.path.append('/root/Group7_Dev_App/Optimal_Performance_Platform')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

# Import models
from home.models import RAM, CPU, Motherboard, Storage, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, Manufacturer, CPUSocketType, StorageFormFactor, StorageCapacity, StorageType, Microarchitecture

fake = Faker()

def create_fake_data():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    microarchitectures = ["Zen 3", "Rocket Lake", "Comet Lake"]

    # Populate Manufacturers
    for name in manufacturers:
        Manufacturer.objects.get_or_create(name=name)

    # Create RAM entries
    for _ in range(10):
        ram_type = RAMType.objects.get_or_create(type=random.choice(ram_types))[0]
        ram_speed = RAMSpeed.objects.get_or_create(speed=random.choice(ram_speeds))[0]
        ram_capacity = RAMCapacity.objects.get_or_create(capacity=random.choice(ram_capacities))[0]
        ram_number_of_modules = RAMNumberOfModules.objects.get_or_create(number_of_modules=random.choice(ram_modules))[0]

        RAM.objects.create(
            ram_type=ram_type,
            ram_speed=ram_speed,
            ram_capacity=ram_capacity,
            ram_number_of_modules=ram_number_of_modules
        )

    # Create CPU entries
    for _ in range(10):
        cpu_manufacturer = Manufacturer.objects.get(name=random.choice(manufacturers))
        cpu_socket = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[0]
        microarch = Microarchitecture.objects.get_or_create(name=random.choice(microarchitectures))[0]

        CPU.objects.create(
            cpu_name=fake.word() + " Processor",
            cpu_manufacturer=cpu_manufacturer,
            cpu_microarchitecture=microarch,
            socket_type=cpu_socket
        )

    # Create Motherboard entries
    for _ in range(10):
        motherboard_manufacturer = Manufacturer.objects.get(name=random.choice(manufacturers))
        socket_type = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[0]
        form_factor = StorageFormFactor.objects.get_or_create(name=random.choice(form_factors))[0]

        motherboard = Motherboard.objects.create(
            name=fake.word() + " Motherboard",
            motherboard_manufacturer=motherboard_manufacturer,
            cpu_socket_type=socket_type,
            memory_slots=random.choice([2, 4]),
            storage_form_factor=form_factor,
            max_memory_capacity=random.choice([64, 128])
        )
        motherboard.supported_ram_types.set(RAMType.objects.filter(type__in=ram_types))
        motherboard.supported_ram_speeds.set(RAMSpeed.objects.filter(speed__in=ram_speeds))

    # Create Storage entries
    for _ in range(10):
        storage_type = StorageType.objects.get_or_create(type=random.choice(storage_types))[0]
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

create_fake_data()
