import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import Manufacturer, StorageType, StorageCapacity, FormFactor, Storage

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class StorageTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers to avoid UNIQUE constraint violations
        cls.manufacturer1 = Manufacturer.objects.create(name="Samsung")
        cls.manufacturer2 = Manufacturer.objects.create(name="Western Digital")

        # Create unique storage type instances
        cls.storage_type1 = StorageType.objects.create(type="SSD")
        cls.storage_type2 = StorageType.objects.create(type="HDD")

        # Create unique storage capacity instances
        cls.storage_capacity1 = StorageCapacity.objects.create(capacity="1TB")
        cls.storage_capacity2 = StorageCapacity.objects.create(capacity="500GB")

        # Create unique form factor instances
        cls.form_factor1 = FormFactor.objects.create(name="2.5 inch")
        cls.form_factor2 = FormFactor.objects.create(name="3.5 inch")

        # Create storage object and assign manufacturer
        cls.storage = Storage.objects.create(
            storage_id=1,
            name='Samsung EVO 860',
            manufacturer=cls.manufacturer1,
            form_factor=cls.form_factor1,
            capacity=cls.storage_capacity1,
            type=cls.storage_type1,
            price=100,
            description="High performance SSD"
        )

    def test_Storage_storage_type_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_Storage_name_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_storage_id(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Storage.objects.create(
                    storage_id=1,  # Duplicate ID
                    name='Duplicate Storage',
                    manufacturer=self.manufacturer2,
                    form_factor=self.form_factor2,
                    capacity=self.storage_capacity2,
                    type=self.storage_type2
                )

    def test_Storage_storage_id_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("storage_id").verbose_name
        self.assertEqual(field_label, "storage id")

    def test_Storage_manufacturer_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("manufacturer").verbose_name
        self.assertEqual(field_label, "manufacturer")

    def test_Storage_object_fields_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info = f"{testObject.name} - {testObject.form_factor.name} - {testObject.capacity.capacity}"
        self.assertEqual(str(testObject), expected_storage_info)

    def test_Storage_object_storage_id_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info = f"{testObject.storage_id}"
        self.assertEqual("1", expected_storage_info)

    def test_Storage_object_storage_manufacturer_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info = f"{testObject.manufacturer.name}"
        self.assertEqual("Samsung", expected_storage_info)

    def test_Storage_object_storage_type_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info = f"{testObject.type.type}"
        self.assertEqual("SSD", expected_storage_info)

    def test_Storage_object_storage_capacity_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info = f"{testObject.capacity.capacity}"
        self.assertEqual("1TB", expected_storage_info)

    # Additional tests
    def test_storage_name_validation(self):
        invalid_storage = Storage(
            storage_id=2,
            name="",  # An empty name should not be allowed
            manufacturer=self.manufacturer2,
            form_factor=self.form_factor2,
            capacity=self.storage_capacity2,
            type=self.storage_type2
        )
        with self.assertRaises(ValidationError):
            invalid_storage.full_clean()  # This should raise a ValidationError

    def test_storage_str(self):
        storage = Storage.objects.get(storage_id=1)
        expected_str = "Samsung EVO 860 - 2.5 inch - 1TB"
        self.assertEqual(str(storage), expected_str)
