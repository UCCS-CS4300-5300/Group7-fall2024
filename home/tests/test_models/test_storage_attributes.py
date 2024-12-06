import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import StorageType, StorageCapacity

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class StorageTypeTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create storage type instances
        cls.storage_type1 = StorageType.objects.create(type="SSD")
        cls.storage_type2 = StorageType.objects.create(type="HDD")

    def test_StorageType_type_field_label(self):
        testObject = StorageType.objects.get(type="SSD")
        field_label = testObject._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_unique_storage_type(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                StorageType.objects.create(type="SSD")  # Duplicate type

    def test_StorageType_object_fields_values(self):
        testObject = StorageType.objects.get(type="SSD")
        expected_storage_type_info = f"{testObject.type}"
        self.assertEqual(str(testObject), expected_storage_type_info)

    def test_storage_type_validation(self):
        invalid_storage_type = StorageType(type="")  # An empty type should not be allowed
        with self.assertRaises(ValidationError):
            invalid_storage_type.full_clean()  # This should raise a ValidationError

    def test_storage_type_str(self):
        storage_type = StorageType.objects.get(type="SSD")
        expected_str = "SSD"
        self.assertEqual(str(storage_type), expected_str)


class StorageCapacityTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create storage capacity instances
        cls.storage_capacity1 = StorageCapacity.objects.create(capacity="1TB")
        cls.storage_capacity2 = StorageCapacity.objects.create(capacity="500GB")

    def test_StorageCapacity_capacity_field_label(self):
        testObject = StorageCapacity.objects.get(capacity="1TB")
        field_label = testObject._meta.get_field("capacity").verbose_name
        self.assertEqual(field_label, "capacity")

    def test_unique_storage_capacity(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                StorageCapacity.objects.create(capacity="1TB")  # Duplicate capacity

    def test_StorageCapacity_object_fields_values(self):
        testObject = StorageCapacity.objects.get(capacity="1TB")
        expected_storage_capacity_info = f"{testObject.capacity}"
        self.assertEqual(str(testObject), expected_storage_capacity_info)

    def test_storage_capacity_validation(self):
        invalid_storage_capacity = StorageCapacity(capacity="")  # An empty capacity should not be allowed
        with self.assertRaises(ValidationError):
            invalid_storage_capacity.full_clean()  # This should raise a ValidationError

    def test_storage_capacity_str(self):
        storage_capacity = StorageCapacity.objects.get(capacity="1TB")
        expected_str = "1TB"
        self.assertEqual(str(storage_capacity), expected_str)
