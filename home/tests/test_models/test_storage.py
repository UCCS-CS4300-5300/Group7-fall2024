from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from home.models import Manufacturer, FormFactor, StorageCapacity, StorageType, Storage


class StorageTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers
        cls.manufacturer1 = Manufacturer.objects.create(name="UniqueIntel")
        cls.manufacturer2 = Manufacturer.objects.create(name="UniqueAMD")

        # Ensure unique FormFactor instances
        cls.form_factor1 = FormFactor.objects.create(name="ATX-Unique1")
        cls.form_factor2 = FormFactor.objects.create(name="MicroATX-Unique2")

        # Ensure unique StorageType instances
        cls.storage_type1 = StorageType.objects.create(type="SSD-Unique1")
        cls.storage_type2 = StorageType.objects.create(type="HDD-Unique2")

        # Create unique StorageCapacity instances
        cls.storage_capacity1 = StorageCapacity.objects.create(capacity="256 GB")
        cls.storage_capacity2 = StorageCapacity.objects.create(capacity="512 GB")

        # Create Storage object and assign manufacturer
        Storage.objects.create(
            storage_id=1,
            name='StorageNameTest',
            manufacturer=cls.manufacturer1,
            form_factor=cls.form_factor1,
            capacity=cls.storage_capacity1,
            type=cls.storage_type1
        )

    def test_Storage_storage_id_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("storage_id").verbose_name
            self.assertEqual(field_label, "storage id")
        else:
            self.fail("Storage object with ID 1 does not exist.")

    def test_Storage_type_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("type").verbose_name
            self.assertEqual(field_label, "type")
        else:
            self.fail("Storage object with ID 1 does not exist.")

    def test_storage_name_validation(self):
        invalid_storage = Storage(
            storage_id=2,
            name='',  # An empty name should not be allowed
            manufacturer=self.manufacturer1,
            form_factor=self.form_factor1,
            capacity=self.storage_capacity1,
            type=self.storage_type1
        )
        with self.assertRaises(ValidationError):
            invalid_storage.full_clean()

    def test_storage_str(self):
        storage = Storage.objects.get(storage_id=1)
        if storage is not None:
            expected_str = f"StorageNameTest - {storage.form_factor.name} - {storage.capacity.capacity}"
            self.assertEqual(str(storage), expected_str)
        else:
            self.fail("Storage object with ID 1 does not exist.")

    def test_unique_storage_id(self):
        with self.assertRaises(IntegrityError):
            Storage.objects.create(
                storage_id=1,  # Duplicate ID
                name='Duplicate Storage',
                manufacturer=self.manufacturer2,
                form_factor=self.form_factor2,
                capacity=self.storage_capacity2,
                type=self.storage_type2
            )
