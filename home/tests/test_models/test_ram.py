import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import Manufacturer, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, RAM

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class RAMTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers to avoid UNIQUE constraint violations
        cls.manufacturer1 = Manufacturer.objects.create(name="Kingston")
        cls.manufacturer2 = Manufacturer.objects.create(name="Corsair")

        # Create unique RAM type instances
        cls.ram_type1 = RAMType.objects.create(type="DDR4")
        cls.ram_type2 = RAMType.objects.create(type="DDR3")

        # Create unique RAM speed instances
        cls.ram_speed1 = RAMSpeed.objects.create(speed=3200)
        cls.ram_speed2 = RAMSpeed.objects.create(speed=2400)

        # Create unique RAM capacity instances
        cls.ram_capacity1 = RAMCapacity.objects.create(capacity="16GB")
        cls.ram_capacity2 = RAMCapacity.objects.create(capacity="8GB")

        # Create unique RAM number of modules instances
        cls.ram_modules1 = RAMNumberOfModules.objects.create(number_of_modules=2)
        cls.ram_modules2 = RAMNumberOfModules.objects.create(number_of_modules=4)

        # Create RAM object and assign manufacturer
        cls.ram = RAM.objects.create(
            ram_id=1,
            name='Kingston HyperX Fury',
            manufacturer=cls.manufacturer1,
            ram_type=cls.ram_type1,
            ram_speed=cls.ram_speed1,
            ram_capacity=cls.ram_capacity1,
            ram_number_of_modules=cls.ram_modules1,
            price=80,
            description="High performance RAM"
        )

    def test_RAM_ram_type_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_type").verbose_name
        self.assertEqual(field_label, "ram type")

    def test_RAM_name_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_ram_id(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                RAM.objects.create(
                    ram_id=1,  # Duplicate ID
                    name='Duplicate RAM',
                    manufacturer=self.manufacturer2,
                    ram_type=self.ram_type2,
                    ram_speed=self.ram_speed2,
                    ram_capacity=self.ram_capacity2,
                    ram_number_of_modules=self.ram_modules2
                )

    def test_RAM_ram_id_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_id").verbose_name
        self.assertEqual(field_label, "ram id")

    def test_RAM_manufacturer_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("manufacturer").verbose_name
        self.assertEqual(field_label, "manufacturer")

    def test_RAM_ram_speed_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_speed").verbose_name
        self.assertEqual(field_label, "ram speed")

    def test_RAM_object_fields_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info = f"{testObject.name} {testObject.ram_type.type} {testObject.ram_speed.speed} MHz - {testObject.ram_number_of_modules.number_of_modules} x {testObject.ram_capacity.capacity}"
        self.assertEqual(str(testObject), expected_RAM_info)

    def test_RAM_object_ram_id_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info = f"{testObject.ram_id}"
        self.assertEqual("1", expected_RAM_info)

    def test_RAM_object_ram_manufacturer_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info = f"{testObject.manufacturer.name}"
        self.assertEqual("Kingston", expected_RAM_info)

    def test_RAM_object_ram_type_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info = f"{testObject.ram_type.type}"
        self.assertEqual("DDR4", expected_RAM_info)

    def test_RAM_object_ram_speed_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info = f"{testObject.ram_speed.speed}"
        self.assertEqual("3200", expected_RAM_info)

    # Additional tests
    def test_ram_name_validation(self):
        invalid_ram = RAM(
            ram_id=2,
            name="",  # An empty name should not be allowed
            manufacturer=self.manufacturer2,
            ram_type=self.ram_type2,
            ram_speed=self.ram_speed2,
            ram_capacity=self.ram_capacity2,
            ram_number_of_modules=self.ram_modules2
        )
        with self.assertRaises(ValidationError):
            invalid_ram.full_clean()  # This should raise a ValidationError

    def test_ram_speed_validation(self):
        invalid_ram = RAM(
            ram_id=3,
            name="Invalid RAM",
            manufacturer=self.manufacturer2,
            ram_type=self.ram_type2,
            ram_speed=RAMSpeed.objects.create(speed=9000),  # Invalid speed
            ram_capacity=self.ram_capacity2,
            ram_number_of_modules=self.ram_modules2
        )
        with self.assertRaises(ValidationError):
            invalid_ram.full_clean()  # This should raise a ValidationError

    def test_ram_str(self):
        ram = RAM.objects.get(ram_id=1)
        expected_str = "Kingston HyperX Fury DDR4 3200 MHz - 2 x 16GB"
        self.assertEqual(str(ram), expected_str)
