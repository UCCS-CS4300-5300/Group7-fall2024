import os
import django
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db import transaction
from home.models import Manufacturer, Microarchitecture, CPUSocketType, CPU

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class CPUTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers to avoid UNIQUE constraint violations
        cls.manufacturer1 = Manufacturer.objects.create(name="UniqueIntel")
        cls.manufacturer2 = Manufacturer.objects.create(name="UniqueAMD")

        # Create unique Microarchitecture instances
        cls.microarchitecture1 = Microarchitecture.objects.create(name="Zen 2")
        cls.microarchitecture2 = Microarchitecture.objects.create(name="Zen 3")

        # Create unique CPUSocketType instances
        cls.cpu_socket_type1 = CPUSocketType.objects.create(name="Socket AM4")
        cls.cpu_socket_type2 = CPUSocketType.objects.create(name="Socket AM5")

        # Create CPU object and assign manufacturer
        cls.cpu = CPU.objects.create(
            cpu_id=1,
            name='Ryzen 3600',
            manufacturer=cls.manufacturer1,
            microarchitecture=cls.microarchitecture1,
            socket_type=cls.cpu_socket_type1,
            price=200,
            description="A powerful CPU"
        )

    def test_CPU_microarchitecture_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("microarchitecture").verbose_name
        self.assertEqual(field_label, "microarchitecture")

    def test_CPU_name_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_unique_cpu_id(self):
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                CPU.objects.create(
                    cpu_id=1,  # Duplicate ID
                    name='Duplicate CPU',
                    manufacturer=self.manufacturer2,
                    microarchitecture=self.microarchitecture2,
                    socket_type=self.cpu_socket_type2
                )

    def test_CPU_cpu_id_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("cpu_id").verbose_name
        self.assertEqual(field_label, "cpu id")

    def test_CPU_manufacturer_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("manufacturer").verbose_name
        self.assertEqual(field_label, "manufacturer")

    def test_CPU_socket_type_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("socket_type").verbose_name
        self.assertEqual(field_label, "socket type")

    def test_CPU_object_fields_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info = f"{testObject.name}"
        self.assertEqual(str(testObject), expected_CPU_info)

    def test_CPU_object_cpu_id_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info = f"{testObject.cpu_id}"
        self.assertEqual("1", expected_CPU_info)

    def test_CPU_object_cpu_manufacturer_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info = f"{testObject.manufacturer.name}"
        self.assertEqual("UniqueIntel", expected_CPU_info)

    def test_CPU_object_cpu_microarchitecture_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info = f"{testObject.microarchitecture.name}"
        self.assertEqual("Zen 2", expected_CPU_info)

    def test_CPU_object_cpu_socket_type_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info = f"{testObject.socket_type.name}"
        self.assertEqual("Socket AM4", expected_CPU_info)

    # Additional tests
    def test_cpu_name_validation(self):
        invalid_cpu = CPU(
            cpu_id=2,
            name="",  # An empty name should not be allowed
            manufacturer=self.manufacturer2,
            microarchitecture=self.microarchitecture2,
            socket_type=self.cpu_socket_type2
        )
        with self.assertRaises(ValidationError):
            invalid_cpu.full_clean()  # This should raise a ValidationError

    def test_cpu_str(self):
        cpu = CPU.objects.get(cpu_id=1)
        expected_str = "Ryzen 3600"
        self.assertEqual(str(cpu), expected_str)
