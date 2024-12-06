import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import Manufacturer

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class ManufacturerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create manufacturer instances
        cls.manufacturer1 = Manufacturer.objects.create(name="Intel")
        cls.manufacturer2 = Manufacturer.objects.create(name="AMD")

    def test_Manufacturer_name_field_label(self):
        testObject = Manufacturer.objects.get(name="Intel")
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_manufacturer_name(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Manufacturer.objects.create(name="Intel")  # Duplicate name

    def test_Manufacturer_object_fields_values(self):
        testObject = Manufacturer.objects.get(name="Intel")
        expected_manufacturer_info = f"{testObject.name}"
        self.assertEqual(str(testObject), expected_manufacturer_info)

    # Additional tests
    def test_manufacturer_name_validation(self):
        invalid_manufacturer = Manufacturer(name="")  # An empty name should not be allowed
        with self.assertRaises(ValidationError):
            invalid_manufacturer.full_clean()  # This should raise a ValidationError

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.get(name="Intel")
        expected_str = "Intel"
        self.assertEqual(str(manufacturer), expected_str)
