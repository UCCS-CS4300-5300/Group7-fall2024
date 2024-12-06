import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError  # Added missing terminator
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import Microarchitecture

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class MicroarchitectureTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create microarchitecture instances
        cls.microarch1 = Microarchitecture.objects.create(name="Zen 2")
        cls.microarch2 = Microarchitecture.objects.create(name="Zen 3")

    def test_Microarchitecture_name_field_label(self):
        testObject = Microarchitecture.objects.get(name="Zen 2")
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_microarchitecture_name(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                Microarchitecture.objects.create(name="Zen 2")  # Duplicate name

    def test_Microarchitecture_object_fields_values(self):
        testObject = Microarchitecture.objects.get(name="Zen 2")
        expected_microarch_info = f"{testObject.name}"
        self.assertEqual(str(testObject), expected_microarch_info)

    # Additional tests
    def test_microarchitecture_name_validation(self):
        invalid_microarch = Microarchitecture(name="")  # An empty name should not be allowed
        with self.assertRaises(ValidationError):
            invalid_microarch.full_clean()  # This should raise a ValidationError

    def test_microarchitecture_str(self):
        microarch = Microarchitecture.objects.get(name="Zen 2")
        expected_str = "Zen 2"
        self.assertEqual(str(microarch), expected_str)
