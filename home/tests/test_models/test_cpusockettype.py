import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import CPUSocketType

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class CPUSocketTypeTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create CPU socket type instances
        cls.socket_type1 = CPUSocketType.objects.create(name="LGA1151")
        cls.socket_type2 = CPUSocketType.objects.create(name="AM4")

    def test_CPUSocketType_name_field_label(self):
        testObject = CPUSocketType.objects.get(name="LGA1151")
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_cpusockettype_name(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                CPUSocketType.objects.create(name="LGA1151")  # Duplicate name

    def test_CPUSocketType_object_fields_values(self):
        testObject = CPUSocketType.objects.get(name="LGA1151")
        expected_socket_type_info = f"{testObject.name}"
        self.assertEqual(str(testObject), expected_socket_type_info)

    # Additional tests
    def test_cpusockettype_name_validation(self):
        invalid_socket_type = CPUSocketType(name="")  # An empty name should not be allowed
        with self.assertRaises(ValidationError):
            invalid_socket_type.full_clean()  # This should raise a ValidationError

    def test_cpusockettype_str(self):
        socket_type = CPUSocketType.objects.get(name="LGA1151")
        expected_str = "LGA1151"
        self.assertEqual(str(socket_type), expected_str)
