from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from home.models import (
    Storage, Manufacturer, FormFactor, StorageType, User, Profile, Build,
    StorageCapacity, RAM, RAMCapacity, RAMNumberOfModules, RAMSpeed, RAMType,
)


class BuildViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        cache.clear()
        User.objects.all().delete()
        Build.objects.all().delete()
        self.user = User.objects.create_user(username='testuser_build', password='testpassword')
        self.profile, created = Profile.objects.get_or_create(user=self.user)
        self.build = Build.objects.create(name="Test Build", profile=self.profile)
        self.client.login(username='testuser_build', password='testpassword')

    def test_search_build_by_user_id(self):
        url = reverse('build-search')
        response = self.client.get(url, {'user_id': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)

    def test_search_build_by_user_username(self):
        url = reverse('build-search')
        response = self.client.get(url, {'user_username': 'testuser_build'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['name'], 'Test Build')

    def test_search_build_invalid_user_id(self):
        url = reverse('build-search')
        response = self.client.get(url, {'user_id': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['user_id'], "user_id must be a valid integer.")


class RAMViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        cache.clear()
        RAM.objects.all().delete()
        RAMSpeed.objects.all().delete()
        RAMType.objects.all().delete()
        RAMCapacity.objects.all().delete()
        RAMNumberOfModules.objects.all().delete()
        Manufacturer.objects.all().delete()
        User.objects.all().delete()

        self.user = User.objects.create_user(username='testuser_ram', password='testpassword')
        self.client.login(username='testuser_ram', password='testpassword')

        self.manufacturer = Manufacturer.objects.create(name='Test Manufacturer')
        self.ram_speed1 = RAMSpeed.objects.create(speed=3200)
        self.ram_speed2 = RAMSpeed.objects.create(speed=3600)
        self.ram_type = RAMType.objects.create(type='DDR4')
        self.ram_capacity1 = RAMCapacity.objects.create(capacity='8GB')
        self.ram_capacity2 = RAMCapacity.objects.create(capacity='16GB')
        self.ram_modules = RAMNumberOfModules.objects.create(number_of_modules=2)

        self.ram1 = RAM.objects.create(
            name='Test RAM 1',
            manufacturer=self.manufacturer,
            ram_type=self.ram_type,
            ram_speed=self.ram_speed1,
            ram_capacity=self.ram_capacity1,
            ram_number_of_modules=self.ram_modules,
            price=100
        )
        self.ram2 = RAM.objects.create(
            name='Test RAM 2',
            manufacturer=self.manufacturer,
            ram_type=self.ram_type,
            ram_speed=self.ram_speed2,
            ram_capacity=self.ram_capacity2,
            ram_number_of_modules=self.ram_modules,
            price=150
        )

    def test_search_ram_by_type(self):
        url = reverse('ram_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'type': 'DDR4'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_search_ram_by_capacity(self):
        url = reverse('ram_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'capacity': '8GB'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['ram_capacity']['capacity'], '8GB')

    def test_search_ram_by_speed(self):
        url = reverse('ram_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'speed': '3600'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['ram_speed']['speed'], 3600)


class StorageViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Clean up any existing data to avoid duplication issues
        cache.clear()
        Storage.objects.all().delete()
        Manufacturer.objects.all().delete()
        FormFactor.objects.all().delete()
        StorageType.objects.all().delete()
        StorageCapacity.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        self.user = User.objects.create_user(username='testuser_storage', password='testpassword')
        Profile.objects.filter(user=self.user).delete()
        self.profile, created = Profile.objects.get_or_create(user=self.user)

        # Create Manufacturer, FormFactor, StorageType, and StorageCapacity instances
        self.manufacturer = Manufacturer.objects.create(name='Test Manufacturer')
        self.form_factor = FormFactor.objects.create(name='Test Form Factor')
        self.storage_type = StorageType.objects.create(type='Test Type')
        self.storage_capacity = StorageCapacity.objects.create(capacity='512GB')

        self.storage = Storage.objects.create(
            manufacturer=self.manufacturer,
            form_factor=self.form_factor,
            type=self.storage_type,
            capacity=self.storage_capacity
        )
        self.client.login(username='testuser_storage', password='testpassword')

    def test_search_storage_by_manufacturer(self):
        url = reverse('storage_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'manufacturer': 'Test Manufacturer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['manufacturer'], self.manufacturer.id)

    def test_search_storage_by_form_factor(self):
        url = reverse('storage_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'form_factor': 'Test Form Factor'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['form_factor']['name'], 'Test Form Factor')

    def test_search_storage_by_type(self):
        url = reverse('storage_search')  # Adjust the reverse name as per your URL configuration
        response = self.client.get(url, {'type': 'Test Type'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['type']['type'], 'Test Type')


class UserBuildViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Clean up any existing data to avoid duplication issues
        cache.clear()  # Clear cache before each test
        Build.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

        # Create a unique user and profile for this test
        self.user = User.objects.create_user(username='testuser_userbuild', password='testpassword')
        # Ensure no duplicate profiles exist
        Profile.objects.filter(user=self.user).delete()
        self.profile = Profile.objects.create(user=self.user)
        self.build = Build.objects.create(name='Test Build', profile=self.profile)
        self.client.login(username='testuser_userbuild', password='testpassword')

    def test_list_user_builds(self):
        """
        Test that only the authenticated user's builds are listed.
        """
        url = reverse('user_builds', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)  # Ensure only one build is returned
        self.assertEqual(response.json()['results'][0]['name'], 'Test Build')

    def test_no_builds_for_unauthenticated_user(self):
        """
        Test that unauthenticated users cannot access the builds.
        """
        self.client.logout()
        url = reverse('user_builds', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_no_other_users_builds(self):
        """
        Test that the user cannot see other users' builds.
        """
        # Create another user and build
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        # Ensure no duplicate profiles exist for the other user
        Profile.objects.filter(user=other_user).delete()
        other_profile = Profile.objects.create(user=other_user)
        Build.objects.create(name='Other User Build', profile=other_profile)

        # Ensure the authenticated user cannot see the other user's build
        url = reverse('user_builds', kwargs={'user_id': self.user.id})
        response = self.client.get(url)

        # build_names = [build['name'] for build in response.json()['results']]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['name'], 'Test Build')
