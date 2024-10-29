from django.test import TestCase
from home.models import *

class StorageTestCase(TestCase):

    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        StorageFormFactor.objects.create(name="ATX")
        StorageCapacity.objects.create(capacity="256 GB")
        StorageType.objects.create(type="SSD")

        Storage.objects.create(storage_id=1,
        name='StorageNameTest',
        storage_form_factor=StorageFormFactor.objects.get(id=1),
        storage_capacity=StorageCapacity.objects.get(id=1),
        storage_type=StorageType.objects.get(id=1))

    # testing the labels of the fields
    def test_Storage_storage_id_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("storage_id").verbose_name
        self.assertEqual(field_label, "storage id")

    def test_Storage_name_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_Storage_form_factor_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("storage_form_factor").verbose_name
        self.assertEqual(field_label, "storage form factor")

    def test_Storage_capacity_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("storage_capacity").verbose_name
        self.assertEqual(field_label, "storage capacity")

    def test_Storage_type_field_label(self):
        testObject = Storage.objects.get(storage_id=1)
        field_label = testObject._meta.get_field("storage_type").verbose_name
        self.assertEqual(field_label, "storage type")

    #testing that fields are assigned expected values
    def test_Storage_object_fields_values(self):
        testObject = Storage.objects.get(storage_id=1)
        expected_storage_info=f"{testObject.name} - {testObject.storage_form_factor.name} - {testObject.storage_capacity.capacity}"
        self.assertEqual(str(testObject), expected_storage_info)

    # add test case to verify contents of name field
    # add test case to verify contents of id field

class CPUTestCase(TestCase):
    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name="Intel")
        Microarchitecture.objects.create(name="Zen 4")
        CPUSocketType.objects.create(name="AM5")

        CPU.objects.create(cpu_id=1,
        cpu_name='CPUNameTest',
        cpu_manufacturer=Manufacturer.objects.get(id=1),
        cpu_microarchitecture=Microarchitecture.objects.get(id=1),
        socket_type=CPUSocketType.objects.get(id=1))

    # testing the labels of the fields
    def test_CPU_CPU_id_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("cpu_id").verbose_name
        self.assertEqual(field_label, "cpu id")

    def test_CPU_name_field_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("cpu_name").verbose_name
        self.assertEqual(field_label, "cpu name")

    def test_CPU_manufacturer_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("cpu_manufacturer").verbose_name
        self.assertEqual(field_label, "cpu manufacturer")

    def test_CPU_microarchitecture_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("cpu_microarchitecture").verbose_name
        self.assertEqual(field_label, "cpu microarchitecture")

    def test_CPU_socket_type_label(self):
        testObject = CPU.objects.get(cpu_id=1)
        field_label = testObject._meta.get_field("socket_type").verbose_name
        self.assertEqual(field_label, "socket type")

    # testing the contents of the name field in CPU objects
    def test_CPU_object_fields_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info=f"{testObject.cpu_name}"
        self.assertEqual(str(testObject), expected_CPU_info)

    # testing the contents of the 