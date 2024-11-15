from django.test import TestCase
from home.models import Manufacturer, CPUSocketType, FormFactor, RAMType, Motherboard
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class MotherboardTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers to avoid UNIQUE constraint violations
        cls.manufacturer1 = Manufacturer.objects.create(name="UniqueIntel")
        cls.manufacturer2 = Manufacturer.objects.create(name="UniqueAMD")

        # Create unique CPUSocketType instances
        cls.cpu_socket_type1 = CPUSocketType.objects.create(name="Socket AM4")
        cls.cpu_socket_type2 = CPUSocketType.objects.create(name="Socket AM5")

        # Ensure unique RAMType instances
        cls.ram_type1 = RAMType.objects.create(type="DDR4-Unique1")
        cls.ram_type2 = RAMType.objects.create(type="DDR5-Unique2")

        # Ensure unique FormFactor instances
        cls.form_factor1 = FormFactor.objects.create(name="ATX-Unique1")
        cls.form_factor2 = FormFactor.objects.create(name="MicroATX-Unique2")

        # Create Motherboard object and assign manufacturer and memory_slots
        cls.motherboard = Motherboard.objects.create(
            motherboard_id=1,
            name='MotherboardNameTest',
            manufacturer=cls.manufacturer1,
            cpu_socket_type=cls.cpu_socket_type1,
            form_factor=cls.form_factor1,
            memory_slots=4,  # Ensure memory_slots is set
            max_memory_capacity=64
        )

        # Assign RAM types to motherboard
        cls.motherboard.supported_ram_types.set([cls.ram_type1, cls.ram_type2])

    def test_motherboard_supported_ram_types_relationship(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            self.assertIn(self.ram_type1, testObject.supported_ram_types.all())
            self.assertIn(self.ram_type2, testObject.supported_ram_types.all())
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_unique_motherboard_id(self):
        with self.assertRaises(IntegrityError):
            Motherboard.objects.create(
                motherboard_id=1,  # Duplicate ID
                name='Duplicate Motherboard',
                manufacturer=self.manufacturer2,
                cpu_socket_type=self.cpu_socket_type2,
                form_factor=self.form_factor2,
                memory_slots=4,
                max_memory_capacity=128
            )

    def test_motherboard_motherboard_id_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("motherboard_id").verbose_name
            self.assertEqual(field_label, "motherboard id")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_name_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("name").verbose_name
            self.assertEqual(field_label, "name")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_manufacturer_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("manufacturer").verbose_name
            self.assertEqual(field_label, "manufacturer")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_cpu_socket_type_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("cpu_socket_type").verbose_name
            self.assertEqual(field_label, "cpu socket type")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_memory_slots_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("memory_slots").verbose_name
            self.assertEqual(field_label, "memory slots")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_form_factor_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("form_factor").verbose_name
            self.assertEqual(field_label, "form factor")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_max_memory_capacity_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("max_memory_capacity").verbose_name
            self.assertEqual(field_label, "max memory capacity")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_supported_ram_types_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("supported_ram_types").verbose_name
            self.assertEqual(field_label, "supported ram types")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    def test_motherboard_supported_ram_speeds_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("supported_ram_speeds").verbose_name
            self.assertEqual(field_label, "supported ram speeds")
        else:
            self.fail("Motherboard object with ID 1 does not exist.")

    # Additional tests
    def test_motherboard_name_validation(self):
        invalid_motherboard = Motherboard(
            motherboard_id=2,
            name="",  # An empty name should not be allowed
            manufacturer=self.manufacturer1,
            cpu_socket_type=self.cpu_socket_type2,
            form_factor=self.form_factor2,
            memory_slots=4,  # Ensure memory_slots is set
            max_memory_capacity=64
        )
        with self.assertRaises(ValidationError):
            invalid_motherboard.full_clean()  # This should raise a ValidationError

    def test_motherboard_str(self):
        motherboard = Motherboard.objects.get(motherboard_id=1)
        if motherboard is not None:
            expected_str = "MotherboardNameTest"
            self.assertEqual(str(motherboard), expected_str)
        else:
            self.fail("Motherboard object with ID 1 does not exist.")
