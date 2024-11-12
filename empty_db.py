from django.contrib.auth.models import User
from home.models import Manufacturer, Microarchitecture, CPUSocketType, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, FormFactor, StorageCapacity, StorageType, RAM, CPU, Motherboard, Build, BuildRAM, Storage, BuildStorageConfiguration, Profile

# Delete all objects from the models
User.objects.all().delete()
Profile.objects.all().delete()
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
RAM.objects.all().delete()
CPU.objects.all().delete()
Motherboard.objects.all().delete()
BuildRAM.objects.all().delete()
Storage.objects.all().delete()
BuildStorageConfiguration.objects.all().delete()
Build.objects.all().delete()

print("Database has been emptied.")
