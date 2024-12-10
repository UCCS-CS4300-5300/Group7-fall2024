# scripts/create_builds.py
import os
import sys
import django
from django.contrib.auth.models import User
from home.models import Profile, Build, Motherboard, CPU, RAM, Storage

print("Starting create_builds.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

# Debugging: Print all storages available
print("List of available storage devices:")
all_storages = Storage.objects.all()
for storage in all_storages:
    print(f" - {storage.name}")

# Users
users = ['testuser', 'dbuck3']

for username in users:
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        # Create Compatible Builds
        builds = [
            {
                'name': f'{username} High-End Build',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='ASUS ROG Zenith II Extreme Alpha'),
                'cpu': CPU.objects.get(name='AMD Ryzen 9 5950X'),
                'ram': [RAM.objects.get(name='G.Skill Ripjaws V 32GB')],
                'storages': [
                    Storage.objects.get(name='Samsung 970 EVO'),
                    Storage.objects.get(name='Seagate IronWolf')
                ]
            },
            {
                'name': f'{username} Mid-Range Build',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='Gigabyte Z690 AORUS MASTER'),
                'cpu': CPU.objects.get(name='Intel Core i7 12700K'),
                'ram': [RAM.objects.get(name='Crucial Ballistix 16GB')],
                'storages': [
                    Storage.objects.get(name='Western Digital Blue'),
                    Storage.objects.get(name='Crucial MX500')
                ]
            },
            {
                'name': f'{username} Budget Build',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='ASUS Prime B450M-A'),
                'cpu': CPU.objects.get(name='AMD Ryzen 5'),
                'ram': [RAM.objects.get(name='Kingston HyperX Fury 8GB')],
                'storages': [Storage.objects.get(name='Samsung 860 EVO')]
            }
        ]

        # Create Incompatible Builds
        incompatible_builds = [
            {
                'name': f'{username} Incompatible Build 1',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='ASUS ROG Strix'),
                'cpu': CPU.objects.get(name='AMD Ryzen 9 5950X'),  # Incompatible CPU for this motherboard
                'ram': [RAM.objects.get(name='G.Skill Ripjaws V 32GB')],
                'storages': [Storage.objects.get(name='Crucial MX500')]
            },
            {
                'name': f'{username} Incompatible Build 2',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='Gigabyte Z690 AORUS MASTER'),
                'cpu': CPU.objects.get(name='Intel Core i5 12600K'),
                'ram': [RAM.objects.get(name='Kingston HyperX Fury 8GB')],  # Incompatible RAM for this motherboard
                'storages': [Storage.objects.get(name='Samsung 860 EVO')]
            }
        ]

        # Create All-Wrong-Parts Build
        all_wrong_builds = [
            {
                'name': f'{username} All Wrong Parts Build',
                'profile': profile,
                'motherboard': Motherboard.objects.get(name='ASRock X570 Taichi'),
                # Incompatible CPU for this motherboard
                'cpu': CPU.objects.get(name='Intel Core i3'),
                # Incompatible RAM type and speed for this motherboard
                'ram': [
                    RAM.objects.get(name='Kingston HyperX Fury 8GB')
                ],
                'storages': [
                    Storage.objects.get(name='Intel Optane 905P')  # Incompatible storage type for this build
                ]
            }
        ]

        print(f"\nCreating builds for {username}...\n")

        for build_data in builds + incompatible_builds + all_wrong_builds:
            try:
                motherboard = build_data['motherboard']
                cpu = build_data['cpu']
                ram = build_data['ram']
                storages = build_data['storages']

                print(f"Motherboard found: {motherboard}")
                print(f"CPU found: {cpu}")
                print(f"RAM found: {ram}")
                print(f"Storages found: {storages}")

                build, created = Build.objects.get_or_create(
                    name=build_data['name'],
                    profile=build_data['profile'],
                    motherboard=motherboard,
                    cpu=cpu,
                    is_complete=True,
                    is_active=False
                )
                if created:
                    build.ram.set(ram)
                    build.storages.set(storages)
                    build.save()
                    print(f"Build {build_data['name']} created for {username}.")
                else:
                    print(f"Build {build_data['name']} already exists for {username}.")

            except Exception as e:
                print(f"Error creating build {build_data['name']} for {username}: {e}")

    except Exception as e:
        print(f"Error creating builds for {username}: {e}")

print("Completed create_builds.py script.")
