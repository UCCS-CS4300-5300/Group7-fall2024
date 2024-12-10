# scripts/empty_db.py
import os
import sys
import django

print("Starting clear_database.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

print("Django setup completed.")

from django.contrib.auth.models import User
from home.models import Manufacturer, Microarchitecture, CPUSocketType, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, FormFactor, StorageCapacity, StorageType, RAM, CPU, Motherboard, Build, BuildRAM, Storage, BuildStorageConfiguration, Profile

def clear_database():
    # Delete all objects from the models
    BuildRAM.objects.all().delete()
    BuildStorageConfiguration.objects.all().delete()
    Build.objects.all().delete()
    RAM.objects.all().delete()
    CPU.objects.all().delete()
    Motherboard.objects.all().delete()
    Storage.objects.all().delete()
    Profile.objects.all().delete()
    User.objects.all().delete()
    Manufacturer.objects.all().delete()
    Microarchitecture.objects.all().delete()
    CPUSocketType.objects.all().delete()
    RAMType.objects.all().delete()
    RAMSpeed.objects.all().delete()
    RAMCapacity.objects.all().delete()
    RAMNumberOfModules.objects.all().delete()
    FormFactor.objects.all().delete()
    StorageCapacity.objects.all().delete()
    StorageType.objects.all().delete()

    print("All specified objects have been deleted from the database.")

if __name__ == "__main__":
    clear_database()

print("Database has been emptied.")
