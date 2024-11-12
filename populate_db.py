from django.contrib.auth.models import User
from home.models import Manufacturer, Microarchitecture, CPUSocketType, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, FormFactor, StorageCapacity, StorageType, RAM, CPU, Motherboard, Build, BuildRAM, Storage, BuildStorageConfiguration, Profile

# Create User and Profile
user, created = User.objects.get_or_create(username='testuser', defaults={'password': 'testpassword'})
profile, created = Profile.objects.get_or_create(user=user, defaults={'profile_name': 'test_profile'})

# Create Manufacturer
manufacturer_asus, created = Manufacturer.objects.get_or_create(name='ASUS')
manufacturer_intel, created = Manufacturer.objects.get_or_create(name='Intel')
manufacturer_kingston, created = Manufacturer.objects.get_or_create(name='Kingston')
manufacturer_samsung, created = Manufacturer.objects.get_or_create(name='Samsung')
manufacturer_wd, created = Manufacturer.objects.get_or_create(name='Western Digital')

# Create Form Factor
form_factor_atx, created = FormFactor.objects.get_or_create(name='ATX')
form_factor_micro_atx, created = FormFactor.objects.get_or_create(name='Micro-ATX')
form_factor_m2, created = FormFactor.objects.get_or_create(name='M.2')
form_factor_2_5, created = FormFactor.objects.get_or_create(name='2.5"')

# Create CPU Socket Type
cpu_socket_lga1151, created = CPUSocketType.objects.get_or_create(name='LGA1151')
cpu_socket_am4, created = CPUSocketType.objects.get_or_create(name='AM4')

# Create Motherboards
motherboard_asus_rog, created = Motherboard.objects.get_or_create(
    name='ASUS ROG Strix',
    manufacturer=manufacturer_asus,
    form_factor=form_factor_atx,
    cpu_socket_type=cpu_socket_lga1151,
    memory_slots=4
)

motherboard_asus_prime, created = Motherboard.objects.get_or_create(
    name='ASUS Prime B450M-A',
    manufacturer=manufacturer_asus,
    form_factor=form_factor_micro_atx,
    cpu_socket_type=cpu_socket_am4,
    memory_slots=2
)

# Create Microarchitectures
microarchitecture_coffee_lake, created = Microarchitecture.objects.get_or_create(name='Coffee Lake')
microarchitecture_ryzen, created = Microarchitecture.objects.get_or_create(name='Zen')

# Create CPUs
cpu_i7_8700k, created = CPU.objects.get_or_create(
    name='Intel Core i7-8700K',
    manufacturer=manufacturer_intel,
    microarchitecture=microarchitecture_coffee_lake,
    socket_type=cpu_socket_lga1151
)

cpu_ryzen_5_3600, created = CPU.objects.get_or_create(
    name='AMD Ryzen 5 3600',
    manufacturer=manufacturer_kingston,
    microarchitecture=microarchitecture_ryzen,
    socket_type=cpu_socket_am4
)

# Create RAM Types
ram_type_ddr4, created = RAMType.objects.get_or_create(type='DDR4')
ram_type_ddr3, created = RAMType.objects.get_or_create(type='DDR3')

# Create RAM Speeds
ram_speed_3200, created = RAMSpeed.objects.get_or_create(speed=3200)
ram_speed_2400, created = RAMSpeed.objects.get_or_create(speed=2400)

# Create RAM Capacities
ram_capacity_16gb, created = RAMCapacity.objects.get_or_create(capacity='16GB')
ram_capacity_8gb, created = RAMCapacity.objects.get_or_create(capacity='8GB')

# Create RAM Number of Modules
ram_modules_2, created = RAMNumberOfModules.objects.get_or_create(number_of_modules=2)
ram_modules_4, created = RAMNumberOfModules.objects.get_or_create(number_of_modules=4)

# Create RAM
ram_kingston_16gb, created = RAM.objects.get_or_create(
    name='Kingston HyperX Fury 16GB',
    manufacturer=manufacturer_kingston,
    ram_type=ram_type_ddr4,
    ram_speed=ram_speed_3200,
    ram_capacity=ram_capacity_16gb,
    ram_number_of_modules=ram_modules_2
)

ram_kingston_8gb, created = RAM.objects.get_or_create(
    name='Kingston HyperX Fury 8GB',
    manufacturer=manufacturer_kingston,
    ram_type=ram_type_ddr3,
    ram_speed=ram_speed_2400,
    ram_capacity=ram_capacity_8gb,
    ram_number_of_modules=ram_modules_4
)

# Create Storage Capacities
capacity_1tb, created = StorageCapacity.objects.get_or_create(capacity='1TB')
capacity_500gb, created = StorageCapacity.objects.get_or_create(capacity='500GB')

# Create Storage Types
type_ssd, created = StorageType.objects.get_or_create(type='SSD')
type_hdd, created = StorageType.objects.get_or_create(type='HDD')

# Create Storages
storage_samsung_970, created = Storage.objects.get_or_create(
    name='Samsung 970 EVO',
    manufacturer=manufacturer_samsung,
    form_factor=form_factor_m2,
    capacity=capacity_1tb,
    type=type_ssd
)

storage_wd_blue, created = Storage.objects.get_or_create(
    name='Western Digital Blue',
    manufacturer=manufacturer_wd,
    form_factor=form_factor_2_5,
    capacity=capacity_500gb,
    type=type_hdd
)

# Create a Build and Associate Components
build, created = Build.objects.get_or_create(
    name='High Performance Build',
    profile=profile,
    motherboard=motherboard_asus_rog,
    cpu=cpu_i7_8700k
)

# Associate RAM with Build
build_ram_16gb, created = BuildRAM.objects.get_or_create(
    build=build,
    ram=ram_kingston_16gb
)

build_ram_8gb, created = BuildRAM.objects.get_or_create(
    build=build,
    ram=ram_kingston_8gb
)

# Associate Storage with Build
build_storage1, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage_samsung_970,
    role='Primary'
)

build_storage2, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage_wd_blue,
    role='Secondary'
)

# Print Results
print('Build:', build)
print('RAM 16GB:', build_ram_16gb)
print('RAM 8GB:', build_ram_8gb)
print('Storage 1:', build_storage1)
print('Storage 2:', build_storage2)
