from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from home.models import Manufacturer, RAMType, RAMSpeed, RAMCapacity, RAMNumberOfModules, RAM


class RAMTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers
        cls.manufacturer1 = Manufacturer.objects.create(name="UniqueIntel")
        cls.manufacturer2 = Manufacturer.objects.create(name="UniqueAMD")

        # Ensure unique RAM types
        cls.ram_type1 = RAMType.objects.create(type="DDR4-Unique1")
        cls.ram_type2 = RAMType.objects.create(type="DDR5-Unique2")

        # Create RAMSpeed, RAMCapacity, and RAMNumberOfModules instances
        cls.ram_speed1 = RAMSpeed.objects.create(speed=3200)
        cls.ram_speed2 = RAMSpeed.objects.create(speed=3600)
        cls.ram_capacity1 = RAMCapacity.objects.create(capacity="16GB")
        cls.ram_capacity2 = RAMCapacity.objects.create(capacity="32GB")
        cls.ram_number_of_modules1 = RAMNumberOfModules.objects.create(number_of_modules=2)
        cls.ram_number_of_modules2 = RAMNumberOfModules.objects.create(number_of_modules=4)

        # Create RAM object
        RAM.objects.create(
            ram_id=1,
            name='RAMNameTest',
            manufacturer=cls.manufacturer1,
            ram_type=cls.ram_type1,
            ram_speed=cls.ram_speed1,
            ram_capacity=cls.ram_capacity1,
            ram_number_of_modules=cls.ram_number_of_modules1
        )

    def test_RAM_ram_id_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("ram_id").verbose_name
            self.assertEqual(field_label, "ram id")
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_type_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("ram_type").verbose_name
            self.assertEqual(field_label, "ram type")
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_speed_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("ram_speed").verbose_name
            self.assertEqual(field_label, "ram speed")
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_capacity_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("ram_capacity").verbose_name
            self.assertEqual(field_label, "ram capacity")
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_number_of_modules_label(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("ram_number_of_modules").verbose_name
            self.assertEqual(field_label, "ram number of modules")
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_object_ram_id_values(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_RAM_info = f"{testObject.ram_id}"
            self.assertEqual("1", expected_RAM_info)
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_RAM_object_fields_values(self):
        testObject = RAM.objects.get(ram_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_RAM_info = f"{testObject.name} {testObject.ram_type.type} {testObject.ram_speed.speed} MHz - {testObject.ram_number_of_modules.number_of_modules} x {testObject.ram_capacity.capacity}"
            self.assertEqual(str(testObject), expected_RAM_info)
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_ram_name_validation(self):
        invalid_ram = RAM(
            ram_id=2,
            name='',  # An empty name should not be allowed
            manufacturer=self.manufacturer1,
            ram_type=self.ram_type1,
            ram_speed=self.ram_speed1,
            ram_capacity=self.ram_capacity1,
            ram_number_of_modules=self.ram_number_of_modules1
        )
        with self.assertRaises(ValidationError):
            invalid_ram.full_clean()

    def test_ram_str(self):
        ram = RAM.objects.get(ram_id=1)
        if ram is not None:
            expected_str = f"RAMNameTest {ram.ram_type.type} {ram.ram_speed.speed} MHz - {ram.ram_number_of_modules.number_of_modules} x {ram.ram_capacity.capacity}"
            self.assertEqual(str(ram), expected_str)
        else:
            self.fail("RAM object with ID 1 does not exist.")

    def test_unique_ram_id(self):
        with self.assertRaises(IntegrityError):
            RAM.objects.create(
                ram_id=1,  # Duplicate ID
                name='Duplicate RAM',
                manufacturer=self.manufacturer2,
                ram_type=self.ram_type2,
                ram_speed=self.ram_speed2,
                ram_capacity=self.ram_capacity2,
                ram_number_of_modules=self.ram_number_of_modules2
            )
