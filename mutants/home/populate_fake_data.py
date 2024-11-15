
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


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

def x_create_fake_data__mutmut_orig():
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

def x_create_fake_data__mutmut_1():
    ram_types = ["XXDDR3XX", "DDR4", "DDR5"]
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

def x_create_fake_data__mutmut_2():
    ram_types = ["DDR3", "XXDDR4XX", "DDR5"]
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

def x_create_fake_data__mutmut_3():
    ram_types = ["DDR3", "DDR4", "XXDDR5XX"]
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

def x_create_fake_data__mutmut_4():
    ram_types = None
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

def x_create_fake_data__mutmut_5():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["XX2133MHzXX", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
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

def x_create_fake_data__mutmut_6():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "XX2400MHzXX", "2666MHz", "3200MHz", "3600MHz"]
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

def x_create_fake_data__mutmut_7():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "XX2666MHzXX", "3200MHz", "3600MHz"]
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

def x_create_fake_data__mutmut_8():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "XX3200MHzXX", "3600MHz"]
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

def x_create_fake_data__mutmut_9():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "XX3600MHzXX"]
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

def x_create_fake_data__mutmut_10():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = None
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

def x_create_fake_data__mutmut_11():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["XX4GBXX", "8GB", "16GB", "32GB"]
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

def x_create_fake_data__mutmut_12():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "XX8GBXX", "16GB", "32GB"]
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

def x_create_fake_data__mutmut_13():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "XX16GBXX", "32GB"]
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

def x_create_fake_data__mutmut_14():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "XX32GBXX"]
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

def x_create_fake_data__mutmut_15():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = None
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

def x_create_fake_data__mutmut_16():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [2, 2, 4]
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

def x_create_fake_data__mutmut_17():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 3, 4]
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

def x_create_fake_data__mutmut_18():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 5]
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

def x_create_fake_data__mutmut_19():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = None
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

def x_create_fake_data__mutmut_20():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["XXIntelXX", "AMD", "Samsung", "Corsair", "Kingston"]
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

def x_create_fake_data__mutmut_21():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "XXAMDXX", "Samsung", "Corsair", "Kingston"]
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

def x_create_fake_data__mutmut_22():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "XXSamsungXX", "Corsair", "Kingston"]
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

def x_create_fake_data__mutmut_23():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "XXCorsairXX", "Kingston"]
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

def x_create_fake_data__mutmut_24():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "XXKingstonXX"]
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

def x_create_fake_data__mutmut_25():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = None
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

def x_create_fake_data__mutmut_26():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["XXLGA1151XX", "AM4", "LGA1200"]
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

def x_create_fake_data__mutmut_27():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "XXAM4XX", "LGA1200"]
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

def x_create_fake_data__mutmut_28():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "XXLGA1200XX"]
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

def x_create_fake_data__mutmut_29():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = None
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

def x_create_fake_data__mutmut_30():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["XXATXXX", "MicroATX", "MiniITX"]
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

def x_create_fake_data__mutmut_31():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "XXMicroATXXX", "MiniITX"]
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

def x_create_fake_data__mutmut_32():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "XXMiniITXXX"]
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

def x_create_fake_data__mutmut_33():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = None
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

def x_create_fake_data__mutmut_34():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["XXSSDXX", "HDD"]
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

def x_create_fake_data__mutmut_35():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "XXHDDXX"]
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

def x_create_fake_data__mutmut_36():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = None
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

def x_create_fake_data__mutmut_37():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["XX128GBXX", "256GB", "512GB", "1TB", "2TB"]
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

def x_create_fake_data__mutmut_38():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "XX256GBXX", "512GB", "1TB", "2TB"]
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

def x_create_fake_data__mutmut_39():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "XX512GBXX", "1TB", "2TB"]
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

def x_create_fake_data__mutmut_40():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "XX1TBXX", "2TB"]
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

def x_create_fake_data__mutmut_41():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "XX2TBXX"]
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

def x_create_fake_data__mutmut_42():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = None
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

def x_create_fake_data__mutmut_43():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    microarchitectures = ["XXZen 3XX", "Rocket Lake", "Comet Lake"]

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

def x_create_fake_data__mutmut_44():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    microarchitectures = ["Zen 3", "XXRocket LakeXX", "Comet Lake"]

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

def x_create_fake_data__mutmut_45():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    microarchitectures = ["Zen 3", "Rocket Lake", "XXComet LakeXX"]

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

def x_create_fake_data__mutmut_46():
    ram_types = ["DDR3", "DDR4", "DDR5"]
    ram_speeds = ["2133MHz", "2400MHz", "2666MHz", "3200MHz", "3600MHz"]
    ram_capacities = ["4GB", "8GB", "16GB", "32GB"]
    ram_modules = [1, 2, 4]
    manufacturers = ["Intel", "AMD", "Samsung", "Corsair", "Kingston"]
    socket_types = ["LGA1151", "AM4", "LGA1200"]
    form_factors = ["ATX", "MicroATX", "MiniITX"]
    storage_types = ["SSD", "HDD"]
    storage_capacities = ["128GB", "256GB", "512GB", "1TB", "2TB"]
    microarchitectures = None

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

def x_create_fake_data__mutmut_47():
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
        Manufacturer.objects.get_or_create(name=None)

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

def x_create_fake_data__mutmut_48():
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
    for _ in range(11):
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

def x_create_fake_data__mutmut_49():
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
        ram_type = RAMType.objects.get_or_create(type=random.choice(None))[0]
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

def x_create_fake_data__mutmut_50():
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
        ram_type = RAMType.objects.get_or_create(type=random.choice(ram_types))[1]
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

def x_create_fake_data__mutmut_51():
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
        ram_type = RAMType.objects.get_or_create(type=random.choice(ram_types))[None]
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

def x_create_fake_data__mutmut_52():
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
        ram_type = None
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

def x_create_fake_data__mutmut_53():
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
        ram_speed = RAMSpeed.objects.get_or_create(speed=random.choice(None))[0]
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

def x_create_fake_data__mutmut_54():
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
        ram_speed = RAMSpeed.objects.get_or_create(speed=random.choice(ram_speeds))[1]
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

def x_create_fake_data__mutmut_55():
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
        ram_speed = RAMSpeed.objects.get_or_create(speed=random.choice(ram_speeds))[None]
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

def x_create_fake_data__mutmut_56():
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
        ram_speed = None
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

def x_create_fake_data__mutmut_57():
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
        ram_capacity = RAMCapacity.objects.get_or_create(capacity=random.choice(None))[0]
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

def x_create_fake_data__mutmut_58():
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
        ram_capacity = RAMCapacity.objects.get_or_create(capacity=random.choice(ram_capacities))[1]
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

def x_create_fake_data__mutmut_59():
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
        ram_capacity = RAMCapacity.objects.get_or_create(capacity=random.choice(ram_capacities))[None]
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

def x_create_fake_data__mutmut_60():
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
        ram_capacity = None
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

def x_create_fake_data__mutmut_61():
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
        ram_number_of_modules = RAMNumberOfModules.objects.get_or_create(number_of_modules=random.choice(None))[0]

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

def x_create_fake_data__mutmut_62():
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
        ram_number_of_modules = RAMNumberOfModules.objects.get_or_create(number_of_modules=random.choice(ram_modules))[1]

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

def x_create_fake_data__mutmut_63():
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
        ram_number_of_modules = RAMNumberOfModules.objects.get_or_create(number_of_modules=random.choice(ram_modules))[None]

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

def x_create_fake_data__mutmut_64():
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
        ram_number_of_modules = None

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

def x_create_fake_data__mutmut_65():
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
            ram_type=None,
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

def x_create_fake_data__mutmut_66():
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
            ram_speed=None,
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

def x_create_fake_data__mutmut_67():
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
            ram_capacity=None,
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

def x_create_fake_data__mutmut_68():
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
            ram_number_of_modules=None
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

def x_create_fake_data__mutmut_69():
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

def x_create_fake_data__mutmut_70():
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

def x_create_fake_data__mutmut_71():
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

def x_create_fake_data__mutmut_72():
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

def x_create_fake_data__mutmut_73():
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
    for _ in range(11):
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

def x_create_fake_data__mutmut_74():
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
        cpu_manufacturer = Manufacturer.objects.get(name=random.choice(None))
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

def x_create_fake_data__mutmut_75():
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
        cpu_manufacturer = None
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

def x_create_fake_data__mutmut_76():
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
        cpu_socket = CPUSocketType.objects.get_or_create(name=random.choice(None))[0]
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

def x_create_fake_data__mutmut_77():
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
        cpu_socket = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[1]
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

def x_create_fake_data__mutmut_78():
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
        cpu_socket = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[None]
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

def x_create_fake_data__mutmut_79():
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
        cpu_socket = None
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

def x_create_fake_data__mutmut_80():
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
        microarch = Microarchitecture.objects.get_or_create(name=random.choice(None))[0]

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

def x_create_fake_data__mutmut_81():
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
        microarch = Microarchitecture.objects.get_or_create(name=random.choice(microarchitectures))[1]

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

def x_create_fake_data__mutmut_82():
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
        microarch = Microarchitecture.objects.get_or_create(name=random.choice(microarchitectures))[None]

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

def x_create_fake_data__mutmut_83():
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
        microarch = None

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

def x_create_fake_data__mutmut_84():
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
            cpu_name=fake.word() - " Processor",
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

def x_create_fake_data__mutmut_85():
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
            cpu_name=fake.word() + "XX ProcessorXX",
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

def x_create_fake_data__mutmut_86():
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
            cpu_manufacturer=None,
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

def x_create_fake_data__mutmut_87():
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
            cpu_microarchitecture=None,
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

def x_create_fake_data__mutmut_88():
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
            socket_type=None
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

def x_create_fake_data__mutmut_89():
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

def x_create_fake_data__mutmut_90():
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

def x_create_fake_data__mutmut_91():
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

def x_create_fake_data__mutmut_92():
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

def x_create_fake_data__mutmut_93():
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
    for _ in range(11):
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

def x_create_fake_data__mutmut_94():
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
        motherboard_manufacturer = Manufacturer.objects.get(name=random.choice(None))
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

def x_create_fake_data__mutmut_95():
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
        motherboard_manufacturer = None
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

def x_create_fake_data__mutmut_96():
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
        socket_type = CPUSocketType.objects.get_or_create(name=random.choice(None))[0]
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

def x_create_fake_data__mutmut_97():
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
        socket_type = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[1]
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

def x_create_fake_data__mutmut_98():
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
        socket_type = CPUSocketType.objects.get_or_create(name=random.choice(socket_types))[None]
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

def x_create_fake_data__mutmut_99():
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
        socket_type = None
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

def x_create_fake_data__mutmut_100():
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
        form_factor = StorageFormFactor.objects.get_or_create(name=random.choice(None))[0]

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

def x_create_fake_data__mutmut_101():
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
        form_factor = StorageFormFactor.objects.get_or_create(name=random.choice(form_factors))[1]

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

def x_create_fake_data__mutmut_102():
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
        form_factor = StorageFormFactor.objects.get_or_create(name=random.choice(form_factors))[None]

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

def x_create_fake_data__mutmut_103():
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
        form_factor = None

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

def x_create_fake_data__mutmut_104():
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
            name=fake.word() - " Motherboard",
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

def x_create_fake_data__mutmut_105():
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
            name=fake.word() + "XX MotherboardXX",
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

def x_create_fake_data__mutmut_106():
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
            motherboard_manufacturer=None,
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

def x_create_fake_data__mutmut_107():
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
            cpu_socket_type=None,
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

def x_create_fake_data__mutmut_108():
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
            memory_slots=random.choice([3, 4]),
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

def x_create_fake_data__mutmut_109():
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
            memory_slots=random.choice([2, 5]),
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

def x_create_fake_data__mutmut_110():
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
            storage_form_factor=None,
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

def x_create_fake_data__mutmut_111():
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
            max_memory_capacity=random.choice([65, 128])
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

def x_create_fake_data__mutmut_112():
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
            max_memory_capacity=random.choice([64, 129])
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

def x_create_fake_data__mutmut_113():
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

def x_create_fake_data__mutmut_114():
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

def x_create_fake_data__mutmut_115():
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

def x_create_fake_data__mutmut_116():
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

def x_create_fake_data__mutmut_117():
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

def x_create_fake_data__mutmut_118():
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

def x_create_fake_data__mutmut_119():
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

        motherboard = None
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

def x_create_fake_data__mutmut_120():
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
        motherboard.supported_ram_types.set(RAMType.objects.filter(type__in=None))
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

def x_create_fake_data__mutmut_121():
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
        motherboard.supported_ram_speeds.set(RAMSpeed.objects.filter(speed__in=None))

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

def x_create_fake_data__mutmut_122():
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
    for _ in range(11):
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

def x_create_fake_data__mutmut_123():
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
        storage_type = StorageType.objects.get_or_create(type=random.choice(None))[0]
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_124():
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
        storage_type = StorageType.objects.get_or_create(type=random.choice(storage_types))[1]
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_125():
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
        storage_type = StorageType.objects.get_or_create(type=random.choice(storage_types))[None]
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_126():
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
        storage_type = None
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_127():
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
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(None))[0]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_128():
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
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[1]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_129():
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
        storage_capacity = StorageCapacity.objects.get_or_create(capacity=random.choice(storage_capacities))[None]
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_130():
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
        storage_capacity = None
        form_factor = StorageFormFactor.objects.get(name=random.choice(form_factors))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_131():
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
        form_factor = StorageFormFactor.objects.get(name=random.choice(None))

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_132():
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
        form_factor = None

        Storage.objects.create(
            name=fake.word() + " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_133():
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
            name=fake.word() - " Storage",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_134():
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
            name=fake.word() + "XX StorageXX",
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_135():
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
            storage_form_factor=None,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_136():
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
            storage_capacity=None,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_137():
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
            storage_type=None
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_138():
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
            storage_form_factor=form_factor,
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_139():
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
            storage_capacity=storage_capacity,
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_140():
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
            storage_type=storage_type
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_141():
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
        )

    print("Fake data created for testing.")

def x_create_fake_data__mutmut_142():
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

    print("XXFake data created for testing.XX")

x_create_fake_data__mutmut_mutants = {
'x_create_fake_data__mutmut_1': x_create_fake_data__mutmut_1, 
    'x_create_fake_data__mutmut_2': x_create_fake_data__mutmut_2, 
    'x_create_fake_data__mutmut_3': x_create_fake_data__mutmut_3, 
    'x_create_fake_data__mutmut_4': x_create_fake_data__mutmut_4, 
    'x_create_fake_data__mutmut_5': x_create_fake_data__mutmut_5, 
    'x_create_fake_data__mutmut_6': x_create_fake_data__mutmut_6, 
    'x_create_fake_data__mutmut_7': x_create_fake_data__mutmut_7, 
    'x_create_fake_data__mutmut_8': x_create_fake_data__mutmut_8, 
    'x_create_fake_data__mutmut_9': x_create_fake_data__mutmut_9, 
    'x_create_fake_data__mutmut_10': x_create_fake_data__mutmut_10, 
    'x_create_fake_data__mutmut_11': x_create_fake_data__mutmut_11, 
    'x_create_fake_data__mutmut_12': x_create_fake_data__mutmut_12, 
    'x_create_fake_data__mutmut_13': x_create_fake_data__mutmut_13, 
    'x_create_fake_data__mutmut_14': x_create_fake_data__mutmut_14, 
    'x_create_fake_data__mutmut_15': x_create_fake_data__mutmut_15, 
    'x_create_fake_data__mutmut_16': x_create_fake_data__mutmut_16, 
    'x_create_fake_data__mutmut_17': x_create_fake_data__mutmut_17, 
    'x_create_fake_data__mutmut_18': x_create_fake_data__mutmut_18, 
    'x_create_fake_data__mutmut_19': x_create_fake_data__mutmut_19, 
    'x_create_fake_data__mutmut_20': x_create_fake_data__mutmut_20, 
    'x_create_fake_data__mutmut_21': x_create_fake_data__mutmut_21, 
    'x_create_fake_data__mutmut_22': x_create_fake_data__mutmut_22, 
    'x_create_fake_data__mutmut_23': x_create_fake_data__mutmut_23, 
    'x_create_fake_data__mutmut_24': x_create_fake_data__mutmut_24, 
    'x_create_fake_data__mutmut_25': x_create_fake_data__mutmut_25, 
    'x_create_fake_data__mutmut_26': x_create_fake_data__mutmut_26, 
    'x_create_fake_data__mutmut_27': x_create_fake_data__mutmut_27, 
    'x_create_fake_data__mutmut_28': x_create_fake_data__mutmut_28, 
    'x_create_fake_data__mutmut_29': x_create_fake_data__mutmut_29, 
    'x_create_fake_data__mutmut_30': x_create_fake_data__mutmut_30, 
    'x_create_fake_data__mutmut_31': x_create_fake_data__mutmut_31, 
    'x_create_fake_data__mutmut_32': x_create_fake_data__mutmut_32, 
    'x_create_fake_data__mutmut_33': x_create_fake_data__mutmut_33, 
    'x_create_fake_data__mutmut_34': x_create_fake_data__mutmut_34, 
    'x_create_fake_data__mutmut_35': x_create_fake_data__mutmut_35, 
    'x_create_fake_data__mutmut_36': x_create_fake_data__mutmut_36, 
    'x_create_fake_data__mutmut_37': x_create_fake_data__mutmut_37, 
    'x_create_fake_data__mutmut_38': x_create_fake_data__mutmut_38, 
    'x_create_fake_data__mutmut_39': x_create_fake_data__mutmut_39, 
    'x_create_fake_data__mutmut_40': x_create_fake_data__mutmut_40, 
    'x_create_fake_data__mutmut_41': x_create_fake_data__mutmut_41, 
    'x_create_fake_data__mutmut_42': x_create_fake_data__mutmut_42, 
    'x_create_fake_data__mutmut_43': x_create_fake_data__mutmut_43, 
    'x_create_fake_data__mutmut_44': x_create_fake_data__mutmut_44, 
    'x_create_fake_data__mutmut_45': x_create_fake_data__mutmut_45, 
    'x_create_fake_data__mutmut_46': x_create_fake_data__mutmut_46, 
    'x_create_fake_data__mutmut_47': x_create_fake_data__mutmut_47, 
    'x_create_fake_data__mutmut_48': x_create_fake_data__mutmut_48, 
    'x_create_fake_data__mutmut_49': x_create_fake_data__mutmut_49, 
    'x_create_fake_data__mutmut_50': x_create_fake_data__mutmut_50, 
    'x_create_fake_data__mutmut_51': x_create_fake_data__mutmut_51, 
    'x_create_fake_data__mutmut_52': x_create_fake_data__mutmut_52, 
    'x_create_fake_data__mutmut_53': x_create_fake_data__mutmut_53, 
    'x_create_fake_data__mutmut_54': x_create_fake_data__mutmut_54, 
    'x_create_fake_data__mutmut_55': x_create_fake_data__mutmut_55, 
    'x_create_fake_data__mutmut_56': x_create_fake_data__mutmut_56, 
    'x_create_fake_data__mutmut_57': x_create_fake_data__mutmut_57, 
    'x_create_fake_data__mutmut_58': x_create_fake_data__mutmut_58, 
    'x_create_fake_data__mutmut_59': x_create_fake_data__mutmut_59, 
    'x_create_fake_data__mutmut_60': x_create_fake_data__mutmut_60, 
    'x_create_fake_data__mutmut_61': x_create_fake_data__mutmut_61, 
    'x_create_fake_data__mutmut_62': x_create_fake_data__mutmut_62, 
    'x_create_fake_data__mutmut_63': x_create_fake_data__mutmut_63, 
    'x_create_fake_data__mutmut_64': x_create_fake_data__mutmut_64, 
    'x_create_fake_data__mutmut_65': x_create_fake_data__mutmut_65, 
    'x_create_fake_data__mutmut_66': x_create_fake_data__mutmut_66, 
    'x_create_fake_data__mutmut_67': x_create_fake_data__mutmut_67, 
    'x_create_fake_data__mutmut_68': x_create_fake_data__mutmut_68, 
    'x_create_fake_data__mutmut_69': x_create_fake_data__mutmut_69, 
    'x_create_fake_data__mutmut_70': x_create_fake_data__mutmut_70, 
    'x_create_fake_data__mutmut_71': x_create_fake_data__mutmut_71, 
    'x_create_fake_data__mutmut_72': x_create_fake_data__mutmut_72, 
    'x_create_fake_data__mutmut_73': x_create_fake_data__mutmut_73, 
    'x_create_fake_data__mutmut_74': x_create_fake_data__mutmut_74, 
    'x_create_fake_data__mutmut_75': x_create_fake_data__mutmut_75, 
    'x_create_fake_data__mutmut_76': x_create_fake_data__mutmut_76, 
    'x_create_fake_data__mutmut_77': x_create_fake_data__mutmut_77, 
    'x_create_fake_data__mutmut_78': x_create_fake_data__mutmut_78, 
    'x_create_fake_data__mutmut_79': x_create_fake_data__mutmut_79, 
    'x_create_fake_data__mutmut_80': x_create_fake_data__mutmut_80, 
    'x_create_fake_data__mutmut_81': x_create_fake_data__mutmut_81, 
    'x_create_fake_data__mutmut_82': x_create_fake_data__mutmut_82, 
    'x_create_fake_data__mutmut_83': x_create_fake_data__mutmut_83, 
    'x_create_fake_data__mutmut_84': x_create_fake_data__mutmut_84, 
    'x_create_fake_data__mutmut_85': x_create_fake_data__mutmut_85, 
    'x_create_fake_data__mutmut_86': x_create_fake_data__mutmut_86, 
    'x_create_fake_data__mutmut_87': x_create_fake_data__mutmut_87, 
    'x_create_fake_data__mutmut_88': x_create_fake_data__mutmut_88, 
    'x_create_fake_data__mutmut_89': x_create_fake_data__mutmut_89, 
    'x_create_fake_data__mutmut_90': x_create_fake_data__mutmut_90, 
    'x_create_fake_data__mutmut_91': x_create_fake_data__mutmut_91, 
    'x_create_fake_data__mutmut_92': x_create_fake_data__mutmut_92, 
    'x_create_fake_data__mutmut_93': x_create_fake_data__mutmut_93, 
    'x_create_fake_data__mutmut_94': x_create_fake_data__mutmut_94, 
    'x_create_fake_data__mutmut_95': x_create_fake_data__mutmut_95, 
    'x_create_fake_data__mutmut_96': x_create_fake_data__mutmut_96, 
    'x_create_fake_data__mutmut_97': x_create_fake_data__mutmut_97, 
    'x_create_fake_data__mutmut_98': x_create_fake_data__mutmut_98, 
    'x_create_fake_data__mutmut_99': x_create_fake_data__mutmut_99, 
    'x_create_fake_data__mutmut_100': x_create_fake_data__mutmut_100, 
    'x_create_fake_data__mutmut_101': x_create_fake_data__mutmut_101, 
    'x_create_fake_data__mutmut_102': x_create_fake_data__mutmut_102, 
    'x_create_fake_data__mutmut_103': x_create_fake_data__mutmut_103, 
    'x_create_fake_data__mutmut_104': x_create_fake_data__mutmut_104, 
    'x_create_fake_data__mutmut_105': x_create_fake_data__mutmut_105, 
    'x_create_fake_data__mutmut_106': x_create_fake_data__mutmut_106, 
    'x_create_fake_data__mutmut_107': x_create_fake_data__mutmut_107, 
    'x_create_fake_data__mutmut_108': x_create_fake_data__mutmut_108, 
    'x_create_fake_data__mutmut_109': x_create_fake_data__mutmut_109, 
    'x_create_fake_data__mutmut_110': x_create_fake_data__mutmut_110, 
    'x_create_fake_data__mutmut_111': x_create_fake_data__mutmut_111, 
    'x_create_fake_data__mutmut_112': x_create_fake_data__mutmut_112, 
    'x_create_fake_data__mutmut_113': x_create_fake_data__mutmut_113, 
    'x_create_fake_data__mutmut_114': x_create_fake_data__mutmut_114, 
    'x_create_fake_data__mutmut_115': x_create_fake_data__mutmut_115, 
    'x_create_fake_data__mutmut_116': x_create_fake_data__mutmut_116, 
    'x_create_fake_data__mutmut_117': x_create_fake_data__mutmut_117, 
    'x_create_fake_data__mutmut_118': x_create_fake_data__mutmut_118, 
    'x_create_fake_data__mutmut_119': x_create_fake_data__mutmut_119, 
    'x_create_fake_data__mutmut_120': x_create_fake_data__mutmut_120, 
    'x_create_fake_data__mutmut_121': x_create_fake_data__mutmut_121, 
    'x_create_fake_data__mutmut_122': x_create_fake_data__mutmut_122, 
    'x_create_fake_data__mutmut_123': x_create_fake_data__mutmut_123, 
    'x_create_fake_data__mutmut_124': x_create_fake_data__mutmut_124, 
    'x_create_fake_data__mutmut_125': x_create_fake_data__mutmut_125, 
    'x_create_fake_data__mutmut_126': x_create_fake_data__mutmut_126, 
    'x_create_fake_data__mutmut_127': x_create_fake_data__mutmut_127, 
    'x_create_fake_data__mutmut_128': x_create_fake_data__mutmut_128, 
    'x_create_fake_data__mutmut_129': x_create_fake_data__mutmut_129, 
    'x_create_fake_data__mutmut_130': x_create_fake_data__mutmut_130, 
    'x_create_fake_data__mutmut_131': x_create_fake_data__mutmut_131, 
    'x_create_fake_data__mutmut_132': x_create_fake_data__mutmut_132, 
    'x_create_fake_data__mutmut_133': x_create_fake_data__mutmut_133, 
    'x_create_fake_data__mutmut_134': x_create_fake_data__mutmut_134, 
    'x_create_fake_data__mutmut_135': x_create_fake_data__mutmut_135, 
    'x_create_fake_data__mutmut_136': x_create_fake_data__mutmut_136, 
    'x_create_fake_data__mutmut_137': x_create_fake_data__mutmut_137, 
    'x_create_fake_data__mutmut_138': x_create_fake_data__mutmut_138, 
    'x_create_fake_data__mutmut_139': x_create_fake_data__mutmut_139, 
    'x_create_fake_data__mutmut_140': x_create_fake_data__mutmut_140, 
    'x_create_fake_data__mutmut_141': x_create_fake_data__mutmut_141, 
    'x_create_fake_data__mutmut_142': x_create_fake_data__mutmut_142
}

def create_fake_data(*args, **kwargs):
    result = _mutmut_trampoline(x_create_fake_data__mutmut_orig, x_create_fake_data__mutmut_mutants, *args, **kwargs)
    return result 

create_fake_data.__signature__ = _mutmut_signature(x_create_fake_data__mutmut_orig)
x_create_fake_data__mutmut_orig.__name__ = 'x_create_fake_data'



create_fake_data()
