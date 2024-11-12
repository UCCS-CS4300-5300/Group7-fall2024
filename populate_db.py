from django.contrib.auth.models import User
from home.models import Manufacturer, Microarchitecture, CPUSocketType, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, FormFactor, StorageCapacity, StorageType, RAM, CPU, Motherboard, Build, BuildRAM, Storage, BuildStorageConfiguration, Profile

# Create User and Profile
user, created = User.objects.get_or_create(username='testuser', defaults={'password': 'testpassword'})
profile, created = Profile.objects.get_or_create(user=user, defaults={'profile_name': 'test_profile'})

# Create Manufacturer
manufacturer, created = Manufacturer.objects.get_or_create(name='ASUS')

# Create Form Factor
form_factor, created = FormFactor.objects.get_or_create(name='ATX')

# Create CPU Socket Type
cpu_socket_type, created = CPUSocketType.objects.get_or_create(name='LGA1151')

# Create Motherboard
motherboard, created = Motherboard.objects.get_or_create(
    name='ASUS ROG Strix',
    manufacturer=manufacturer,
    form_factor=form_factor,
    cpu_socket_type=cpu_socket_type,
    memory_slots=4
)

# Create Microarchitecture
microarchitecture, created = Microarchitecture.objects.get_or_create(name='Coffee Lake')

# Create CPU
cpu, created = CPU.objects.get_or_create(
    name='Intel Core i7-8700K',
    manufacturer=manufacturer,
    microarchitecture=microarchitecture,
    socket_type=cpu_socket_type
)

# Create RAM Type
ram_type, created = RAMType.objects.get_or_create(type='DDR4')

# Create RAM Speed
ram_speed, created = RAMSpeed.objects.get_or_create(speed=3200)

# Create RAM Capacity
ram_capacity, created = RAMCapacity.objects.get_or_create(capacity='16GB')

# Create RAM Number of Modules
ram_modules, created = RAMNumberOfModules.objects.get_or_create(number_of_modules=2)

# Create RAM
ram1, created = RAM.objects.get_or_create(
    name='Kingston HyperX Fury',
    manufacturer=manufacturer,
    ram_type=ram_type,
    ram_speed=ram_speed,
    ram_capacity=ram_capacity,
    ram_number_of_modules=ram_modules
)

# Create Primary Storage
manufacturer1, created = Manufacturer.objects.get_or_create(name='Samsung')
form_factor1, created = FormFactor.objects.get_or_create(name='M.2')
capacity1, created = StorageCapacity.objects.get_or_create(capacity='1TB')
type1, created = StorageType.objects.get_or_create(type='SSD')

storage1, created = Storage.objects.get_or_create(
    name='Samsung 970 EVO',
    manufacturer=manufacturer1,
    form_factor=form_factor1,
    capacity=capacity1,
    type=type1
)

# Create Secondary Storage
manufacturer2, created = Manufacturer.objects.get_or_create(name='Western Digital')
form_factor2, created = FormFactor.objects.get_or_create(name='2.5"')
capacity2, created = StorageCapacity.objects.get_or_create(capacity='500GB')
type2, created = StorageType.objects.get_or_create(type='HDD')

storage2, created = Storage.objects.get_or_create(
    name='Western Digital Blue',
    manufacturer=manufacturer2,
    form_factor=form_factor2,
    capacity=capacity2,
    type=type2
)

# Create Build and Associate Components
build, created = Build.objects.get_or_create(
    name='High Performance Build',
    profile=profile,
    motherboard=motherboard,
    cpu=cpu
)

# Associate RAM with Build
build_ram, created = BuildRAM.objects.get_or_create(
    build=build,
    ram=ram1
)

# Associate Storage with Build
build_storage1, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage1,
    role='Primary'
)

build_storage2, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage2,
    role='Secondary'
)

# Print Results
print('Build:', build)
print('RAM:', build_ram)
print('Storage 1:', build_storage1)
print('Storage 2:', build_storage2)
