from django.test import TestCase
from home.models import Manufacturer, Microarchitecture, CPUSocketType, CPU
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

class CPUTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create unique manufacturers to avoid UNIQUE constraint violations
        print("Creating manufacturers...")
        cls.manufacturer1 = Manufacturer.objects.create(name="UniqueIntel")
        cls.manufacturer2 = Manufacturer.objects.create(name="UniqueAMD")
        print("Manufacturers created:", cls.manufacturer1, cls.manufacturer2)

        # Create unique Microarchitecture instances
        print("Creating microarchitectures...")
        cls.microarchitecture1 = Microarchitecture.objects.create(name="Zen 2")
        cls.microarchitecture2 = Microarchitecture.objects.create(name="Zen 3")
        print("Microarchitectures created:", cls.microarchitecture1, cls.microarchitecture2)

        # Create unique CPUSocketType instances
        print("Creating CPU socket types...")
        cls.cpu_socket_type1 = CPUSocketType.objects.create(name="Socket AM4")
        cls.cpu_socket_type2 = CPUSocketType.objects.create(name="Socket AM5")
        print("CPU socket types created:", cls.cpu_socket_type1, cls.cpu_socket_type2)

        # Create CPU object and assign manufacturer
        print("Creating CPU...")
        cls.cpu = CPU.objects.create(
            cpu_id=1,
            name='Ryzen 3600',
            manufacturer=cls.manufacturer1,
            microarchitecture=cls.microarchitecture1,
            socket_type=cls.cpu_socket_type1
        )
        print("CPU created:", cls.cpu)

    def test_CPU_microarchitecture_field_label(self):
        print("Running test_CPU_microarchitecture_field_label...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("microarchitecture").verbose_name
            self.assertEqual(field_label, "microarchitecture")
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_name_field_label(self):
        print("Running test_CPU_name_field_label...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("name").verbose_name
            self.assertEqual(field_label, "name")
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_unique_cpu_id(self):
        print("Running test_unique_cpu_id...")
        with self.assertRaises(IntegrityError):
            CPU.objects.create(
                cpu_id=1,  # Duplicate ID
                name='Duplicate CPU',
                manufacturer=self.manufacturer2,
                microarchitecture=self.microarchitecture2,
                socket_type=self.cpu_socket_type2
            )

    def test_CPU_cpu_id_field_label(self):
        print("Running test_CPU_cpu_id_field_label...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("cpu_id").verbose_name
            self.assertEqual(field_label, "cpu id")
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_manufacturer_field_label(self):
        print("Running test_CPU_manufacturer_field_label...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("manufacturer").verbose_name
            self.assertEqual(field_label, "manufacturer")
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_socket_type_field_label(self):
        print("Running test_CPU_socket_type_field_label...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            field_label = testObject._meta.get_field("socket_type").verbose_name
            self.assertEqual(field_label, "socket type")
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_object_fields_values(self):
        print("Running test_CPU_object_fields_values...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_CPU_info = f"{testObject.name}"
            self.assertEqual(str(testObject), expected_CPU_info)
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_object_cpu_id_values(self):
        print("Running test_CPU_object_cpu_id_values...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_CPU_info = f"{testObject.cpu_id}"
            self.assertEqual("1", expected_CPU_info)
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_object_cpu_manufacturer_values(self):
        print("Running test_CPU_object_cpu_manufacturer_values...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_CPU_info = f"{testObject.manufacturer.name}"
            self.assertEqual("UniqueIntel", expected_CPU_info)
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_object_cpu_microarchitecture_values(self):
        print("Running test_CPU_object_cpu_microarchitecture_values...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_CPU_info = f"{testObject.microarchitecture.name}"
            self.assertEqual("Zen 2", expected_CPU_info)
        else:
            self.fail("CPU object with ID 1 does not exist.")

    def test_CPU_object_cpu_socket_type_values(self):
        print("Running test_CPU_object_cpu_socket_type_values...")
        testObject = CPU.objects.get(cpu_id=1)
        if testObject is not None:
            print("testObject found:", testObject)
            expected_CPU_info = f"{testObject.socket_type.name}"
            self.assertEqual("Socket AM4", expected_CPU_info)
        else:
            self.fail("CPU object with ID 1 does not exist.")

    # Additional tests
    def test_cpu_name_validation(self):
        print("Running test_cpu_name_validation...")
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
        print("Running test_cpu_str...")
        cpu = CPU.objects.get(cpu_id=1)
        if cpu is not None:
            print("cpu found:", cpu)
            expected_str = "Ryzen 3600"
            self.assertEqual(str(cpu), expected_str)
        else:
            self.fail("CPU object with ID 1 does not exist.")
