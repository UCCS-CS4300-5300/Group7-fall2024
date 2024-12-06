import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import FormFactor

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class FormFactorTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create form factor instances
        cls.form_factor1 = FormFactor.objects.create(name="2.5 inch")
        cls.form_factor2 = FormFactor.objects.create(name="3.5 inch")

    def test_FormFactor_name_field_label(self):
        testObject = FormFactor.objects.get(name="2.5 inch")
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_formfactor_name(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                FormFactor.objects.create(name="2.5 inch")  # Duplicate name

    def test_FormFactor_object_fields_values(self):
        testObject = FormFactor.objects.get(name="2.5 inch")
        expected_formfactor_info = f"{testObject.name}"
        self.assertEqual(str(testObject), expected_formfactor_info)

    # Additional tests
    def test_formfactor_name_validation(self):
        invalid_formfactor = FormFactor(name="")  # An empty name should not be allowed
        with self.assertRaises(ValidationError):
            invalid_formfactor.full_clean()  # This should raise a ValidationError

    def test_formfactor_str(self):
        formfactor = FormFactor.objects.get(name="2.5 inch")
        expected_str = "2.5 inch"
        self.assertEqual(str(formfactor), expected_str)
