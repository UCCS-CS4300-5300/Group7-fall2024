import os
import django
from django.test import TestCase
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from home.models import (
    create_profile, Profile, Manufacturer, CPUSocketType,
    Microarchitecture, CPU, RAMType, RAMSpeed
)
from home.models import (
    RAMCapacity, RAMNumberOfModules, RAM,
    StorageType, StorageCapacity, Storage, Motherboard, FormFactor
)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class MotherboardModelTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        post_save.disconnect(create_profile, sender=User)

    @classmethod
    def tearDownClass(cls):
        post_save.connect(create_profile, sender=User)
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user, profile_name='Test Profile')
        self.manufacturer = Manufacturer.objects.create(name="Intel")
        self.cpu_socket = CPUSocketType.objects.create(name="LGA1151")
        self.microarchitecture = Microarchitecture.objects.create(name="Comet Lake")
        self.cpu = CPU.objects.create(name="Intel Core i5", manufacturer=self.manufacturer,
                                      microarchitecture=self.microarchitecture, socket_type=self.cpu_socket)
        self.ram_type = RAMType.objects.create(type="DDR4")
        self.ram_speed = RAMSpeed.objects.create(speed=2666)
        self.ram_capacity = RAMCapacity.objects.create(capacity="8GB")
        self.ram_modules = RAMNumberOfModules.objects.create(number_of_modules=2)
        self.ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                      ram_capacity=self.ram_capacity, ram_number_of_modules=self.ram_modules,
                                      manufacturer=self.manufacturer)
        self.storage_type = StorageType.objects.create(type="SSD")
        self.storage_capacity = StorageCapacity.objects.create(capacity="512GB")
        self.storage_form_factor = FormFactor.objects.create(name="2.5 inch")
        self.storage = Storage.objects.create(name="Samsung SSD", form_factor=self.storage_form_factor,
                                              capacity=self.storage_capacity, type=self.storage_type,
                                              manufacturer=self.manufacturer, price=100)
        self.motherboard = Motherboard.objects.create(name="ASUS Prime", manufacturer=self.manufacturer,
                                                      cpu_socket_type=self.cpu_socket, memory_slots=2,
                                                      form_factor=self.storage_form_factor,
                                                      max_memory_capacity=64, price=150)
        self.motherboard.supported_ram_types.add(self.ram_type)
        self.motherboard.supported_ram_speeds.add(self.ram_speed)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.profile_name, 'Test Profile')

    def test_cpu_creation(self):
        self.assertEqual(self.cpu.name, "Intel Core i5")
        self.assertEqual(self.cpu.manufacturer.name, "Intel")

    def test_motherboard_ram_compatibility(self):
        self.assertTrue(self.motherboard.is_ram_compatible(self.ram))

    def test_motherboard_cpu_compatibility(self):
        self.assertTrue(self.motherboard.is_cpu_compatible(self.cpu))

    def test_motherboard_storage_compatibility(self):
        self.assertTrue(self.motherboard.is_storage_compatible(self.storage))

    def test_incompatible_ram_capacity(self):
        incompatible_ram_capacity = RAMCapacity.objects.create(capacity="128GB")
        ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=incompatible_ram_capacity, ram_number_of_modules=self.ram_modules,
                                 manufacturer=self.manufacturer)
        self.assertFalse(self.motherboard.is_ram_compatible(ram))

    def test_incompatible_ram_type(self):
        incompatible_ram_type = RAMType.objects.create(type="DDR3")
        ram = RAM.objects.create(ram_type=incompatible_ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=self.ram_capacity, ram_number_of_modules=self.ram_modules,
                                 manufacturer=self.manufacturer)
        self.assertFalse(self.motherboard.is_ram_compatible(ram))

    def test_max_ram_capacity_compatibility(self):
        max_ram_capacity = RAMCapacity.objects.create(capacity="64GB")
        ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=max_ram_capacity, ram_number_of_modules=self.ram_modules,
                                 manufacturer=self.manufacturer)
        self.assertTrue(self.motherboard.is_ram_compatible(ram))

    def test_min_ram_capacity_compatibility(self):
        min_ram_capacity = RAMCapacity.objects.create(capacity="1GB")
        ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=min_ram_capacity, ram_number_of_modules=self.ram_modules,
                                 manufacturer=self.manufacturer)
        self.assertTrue(self.motherboard.is_ram_compatible(ram))

    def test_default_max_memory_capacity(self):
        motherboard = Motherboard.objects.create(name="Default Motherboard", manufacturer=self.manufacturer,
                                                 cpu_socket_type=self.cpu_socket, memory_slots=2,
                                                 form_factor=self.storage_form_factor, price=150)
        self.assertEqual(motherboard.max_memory_capacity, 128)

    def test_default_price(self):
        motherboard = Motherboard.objects.create(name="Cheap Motherboard", manufacturer=self.manufacturer,
                                                 cpu_socket_type=self.cpu_socket, memory_slots=2,
                                                 form_factor=self.storage_form_factor, max_memory_capacity=64)
        self.assertEqual(motherboard.price, 0)

    def test_motherboard_str(self):
        self.assertEqual(str(self.motherboard), "ASUS Prime")

    def test_motherboard_has_supported_ram_types(self):
        self.assertIn(self.ram_type, self.motherboard.supported_ram_types.all())

    def test_motherboard_has_supported_ram_speeds(self):
        self.assertIn(self.ram_speed, self.motherboard.supported_ram_speeds.all())
