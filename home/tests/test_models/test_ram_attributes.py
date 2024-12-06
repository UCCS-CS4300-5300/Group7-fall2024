import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class RAMTypeTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ram_type1 = RAMType.objects.create(type="DDR4")
        cls.ram_type2 = RAMType.objects.create(type="DDR3")

    def test_RAMType_type_field_label(self):
        testObject = RAMType.objects.get(type="DDR4")
        field_label = testObject._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_unique_ram_type(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                RAMType.objects.create(type="DDR4")

    def test_RAMType_object_fields_values(self):
        testObject = RAMType.objects.get(type="DDR4")
        expected_ram_type_info = f"{testObject.type}"
        self.assertEqual(str(testObject), expected_ram_type_info)

    def test_ram_type_validation(self):
        invalid_ram_type = RAMType(type="")
        with self.assertRaises(ValidationError):
            invalid_ram_type.full_clean()

    def test_ram_type_str(self):
        ram_type = RAMType.objects.get(type="DDR4")
        expected_str = "DDR4"
        self.assertEqual(str(ram_type), expected_str)


class RAMSpeedTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ram_speed1 = RAMSpeed.objects.create(speed=3200)
        cls.ram_speed2 = RAMSpeed.objects.create(speed=2400)

    def test_RAMSpeed_speed_field_label(self):
        testObject = RAMSpeed.objects.get(speed=3200)
        field_label = testObject._meta.get_field("speed").verbose_name
        self.assertEqual(field_label, "speed")

    def test_RAMSpeed_object_fields_values(self):
        testObject = RAMSpeed.objects.get(speed=3200)
        expected_ram_speed_info = f"{testObject.speed} MHz"
        self.assertEqual(str(testObject), expected_ram_speed_info)

    def test_ram_speed_validation(self):
        invalid_ram_speed = RAMSpeed(speed=750)
        with self.assertRaises(ValidationError):
            invalid_ram_speed.full_clean()

    def test_ram_speed_str(self):
        ram_speed = RAMSpeed.objects.get(speed=3200)
        expected_str = "3200 MHz"
        self.assertEqual(str(ram_speed), expected_str)


class RAMCapacityTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ram_capacity1 = RAMCapacity.objects.create(capacity="16GB")
        cls.ram_capacity2 = RAMCapacity.objects.create(capacity="8GB")

    def test_unique_ram_capacity(self):
        initial_count = RAMCapacity.objects.filter(capacity="16GB").count()
        self.assertEqual(initial_count, 1)  # Ensure there is initially one object with capacity "16GB"

        try:
            with transaction.atomic():
                RAMCapacity.objects.create(capacity="16GB")
        except IntegrityError:
            pass  # Expected behavior
        else:
            self.fail("IntegrityError not raised when creating a duplicate RAM capacity")

        final_count = RAMCapacity.objects.filter(capacity="16GB").count()
        self.assertEqual(final_count, 1)  # Ensure no duplicate entry was created

    def test_RAMCapacity_capacity_field_label(self):
        testObject = RAMCapacity.objects.get(capacity="16GB")
        field_label = testObject._meta.get_field("capacity").verbose_name
        self.assertEqual(field_label, "capacity")

    def test_RAMCapacity_object_fields_values(self):
        testObject = RAMCapacity.objects.get(capacity="16GB")
        expected_ram_capacity_info = f"{testObject.capacity}"
        self.assertEqual(str(testObject), expected_ram_capacity_info)

    def test_ram_capacity_validation(self):
        invalid_ram_capacity = RAMCapacity(capacity="")
        with self.assertRaises(ValidationError):
            invalid_ram_capacity.full_clean()

    def test_ram_capacity_str(self):
        ram_capacity = RAMCapacity.objects.get(capacity="16GB")
        expected_str = "16GB"
        self.assertEqual(str(ram_capacity), expected_str)


class RAMNumberOfModulesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.ram_modules1 = RAMNumberOfModules.objects.create(number_of_modules=2)
        cls.ram_modules2 = RAMNumberOfModules.objects.create(number_of_modules=4)

    def test_RAMNumberOfModules_object_fields_values(self):
        testObject = RAMNumberOfModules.objects.get(number_of_modules=2)
        expected_ram_modules_info = 2
        self.assertEqual(testObject.number_of_modules, expected_ram_modules_info)

    def test_RAMNumberOfModules_object_fields_values_integer(self):
        testObject = RAMNumberOfModules.objects.get(number_of_modules=2)
        self.assertEqual(testObject.number_of_modules, 2)

    def test_ram_number_of_modules_validation(self):
        invalid_ram_modules = RAMNumberOfModules(number_of_modules=0)
        with self.assertRaises(ValidationError):
            invalid_ram_modules.full_clean()
