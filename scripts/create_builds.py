# scripts/create_builds.py
import os
import sys
import django

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

from django.contrib.auth.models import User
from home.models import Profile, Build, BuildRAM, BuildStorageConfiguration, RAM, CPU, Storage, Motherboard

# Create Builds
user = User.objects.get(username='testuser')
profile = Profile.objects.get(user=user)
motherboard_asus_rog = Motherboard.objects.get(name='ASUS ROG Strix')
cpu_i7_8700k = CPU.objects.get(name='Intel Core i7-8700K')

build, created = Build.objects.get_or_create(
    name='High Performance Build',
    profile=profile,
    motherboard=motherboard_asus_rog,
    cpu=cpu_i7_8700k,
    is_complete=True,
    is_active=True
)

# Associate RAM with Build
ram_kingston_16gb = RAM.objects.get(name='Kingston HyperX Fury 16GB')
ram_kingston_8gb = RAM.objects.get(name='Kingston HyperX Fury 8GB')

build_ram_16gb, created = BuildRAM.objects.get_or_create(
    build=build,
    ram=ram_kingston_16gb
)

build_ram_8gb, created = BuildRAM.objects.get_or_create(
    build=build,
    ram=ram_kingston_8gb
)

# Associate Storage with Build
storage_samsung_970 = Storage.objects.get(name='Samsung 970 EVO')
storage_wd_blue = Storage.objects.get(name='Western Digital Blue')

build_storage_970, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage_samsung_970,
    role='Primary'
)

build_storage_wd, created = BuildStorageConfiguration.objects.get_or_create(
    build=build,
    storage=storage_wd_blue,
    role='Secondary'
)

# Print Results
print('Build:', build)
print('Build RAM Associations:', build_ram_16gb, build_ram_8gb)
print('Build Storage Associations:', build_storage_970, build_storage_wd)
