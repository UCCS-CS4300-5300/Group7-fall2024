# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

class ModelTests(TestCase):
    
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
        self.cpu = CPU.objects.create(cpu_name="Intel Core i5", cpu_manufacturer=self.manufacturer,
                                      cpu_microarchitecture=self.microarchitecture, socket_type=self.cpu_socket)
        self.ram_type = RAMType.objects.create(type="DDR4")
        self.ram_speed = RAMSpeed.objects.create(speed="2666MHz")
        self.ram_capacity = RAMCapacity.objects.create(capacity="8GB")
        self.ram_modules = RAMNumberOfModules.objects.create(number_of_modules=2)
        self.ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                      ram_capacity=self.ram_capacity, ram_number_of_modules=self.ram_modules)
        self.storage_type = StorageType.objects.create(type="SSD")
        self.storage_capacity = StorageCapacity.objects.create(capacity="512GB")
        self.storage_form_factor = StorageFormFactor.objects.create(name="2.5 inch")
        self.storage = Storage.objects.create(name="Samsung SSD", storage_form_factor=self.storage_form_factor,
                                              storage_capacity=self.storage_capacity, storage_type=self.storage_type)
        self.motherboard = Motherboard.objects.create(name="ASUS Prime", motherboard_manufacturer=self.manufacturer,
                                                      cpu_socket_type=self.cpu_socket, memory_slots=2,
                                                      storage_form_factor=self.storage_form_factor,
                                                      max_memory_capacity=64)
        self.motherboard.supported_ram_types.add(self.ram_type)
        self.motherboard.supported_ram_speeds.add(self.ram_speed)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.profile_name, 'Test Profile')

    def test_cpu_creation(self):
        self.assertEqual(self.cpu.cpu_name, "Intel Core i5")
        self.assertEqual(self.cpu.cpu_manufacturer.name, "Intel")

    def test_motherboard_ram_compatibility(self):
        self.assertTrue(self.motherboard.is_ram_compatible(self.ram))

    def test_motherboard_cpu_compatibility(self):
        self.assertTrue(self.motherboard.is_cpu_compatible(self.cpu))

    def test_motherboard_storage_compatibility(self):
        self.assertTrue(self.motherboard.is_storage_compatible(self.storage))

    def test_incompatible_ram_capacity(self):
        incompatible_ram_capacity = RAMCapacity.objects.create(capacity="128GB")
        ram = RAM.objects.create(ram_type=self.ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=incompatible_ram_capacity, ram_number_of_modules=self.ram_modules)
        self.assertFalse(self.motherboard.is_ram_compatible(ram))

    def test_incompatible_ram_type(self):
        incompatible_ram_type = RAMType.objects.create(type="DDR3")
        ram = RAM.objects.create(ram_type=incompatible_ram_type, ram_speed=self.ram_speed,
                                 ram_capacity=self.ram_capacity, ram_number_of_modules=self.ram_modules)
        self.assertFalse(self.motherboard.is_ram_compatible(ram))

class ViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login_view(self):
        response = self.client.get(reverse('login_or_register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('index'))

    def test_search_pc_parts(self):
        response = self.client.get(reverse('search_pc_parts'), {'q': 'Intel', 'category': 'CPU'})
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_build_view(self):
        response = self.client.get(reverse('build'))
        self.assertEqual(response.status_code, 200)

    def test_pre_built_view(self):
        response = self.client.get(reverse('pre_build'))
        self.assertEqual(response.status_code, 200)
