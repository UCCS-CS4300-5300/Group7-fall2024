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

    # testing the value of cpu_id
    def test_CPU_object_CPU_id_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info=f"{testObject.cpu_id}"
        self.assertEqual("1", expected_CPU_info)

    # testing the value of cpu_manufacturer
    def test_CPU_object_CPU_manufacturer_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info=f"{testObject.cpu_manufacturer.name}"
        self.assertEqual("Intel", expected_CPU_info)

    # testing the value of cpu_manufacturer
    def test_CPU_object_CPU_microarchitecture_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info=f"{testObject.cpu_microarchitecture.name}"
        self.assertEqual("Zen 4", expected_CPU_info)

    # testing the value of socket_type
    def test_CPU_object_CPU_socket_type_values(self):
        testObject = CPU.objects.get(cpu_id=1)
        expected_CPU_info=f"{testObject.socket_type.name}"
        self.assertEqual("AM5", expected_CPU_info)

class RAMTestCase(TestCase):
    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # create objects necesary to create a ram object
        RAMType.objects.create(type="DDR4")
        RAMSpeed.objects.create(speed="3200MHz")
        RAMCapacity.objects.create(capacity="16GB")
        RAMNumberOfModules.objects.create(number_of_modules=2)

        # create ram object and establish relationships
        RAM.objects.create(ram_id=1,
        ram_type=RAMType.objects.get(id=1),
        ram_speed=RAMSpeed.objects.get(id=1),
        ram_capacity=RAMCapacity.objects.get(id=1),
        ram_number_of_modules=RAMNumberOfModules.objects.get(id=1))

        # testing the labels of the fields
    def test_RAM_Ram_id_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_id").verbose_name
        self.assertEqual(field_label, "ram id")

    def test_RAM_type_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_type").verbose_name
        self.assertEqual(field_label, "ram type")

    def test_RAM_speed_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_speed").verbose_name
        self.assertEqual(field_label, "ram speed")

    def test_RAM_capacity_field_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_capacity").verbose_name
        self.assertEqual(field_label, "ram capacity")

    def test_RAM_number_of_modules_label(self):
        testObject = RAM.objects.get(ram_id=1)
        field_label = testObject._meta.get_field("ram_number_of_modules").verbose_name
        self.assertEqual(field_label, "ram number of modules")

    # testing the value of ram_id
    def test_RAM_object_RAM_id_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_RAM_info=f"{testObject.ram_id}"
        self.assertEqual("1", expected_RAM_info)

    # testing the values of the ram_type, ram_speed, ram_capacity, and ram_number_of_modules
    def test_RAM_object_fields_values(self):
        testObject = RAM.objects.get(ram_id=1)
        expected_storage_info=f"{testObject.ram_type} {testObject.ram_speed} - {testObject.ram_number_of_modules} x {testObject.ram_capacity}"
        self.assertEqual(str(testObject), expected_storage_info)

class MotherboardTestCase(TestCase):
    # Set up non-modified objects used by all test methods
    @classmethod
    def setUpTestData(cls):
        # create objects necesary to create a ram object
        Manufacturer.objects.create(name="Intel")
        CPUSocketType.objects.create(name="AM5")
        StorageFormFactor.objects.create(name="ATX")
        RAMNumberOfModules.objects.create(number_of_modules=2)
        # two ramTypes to test many to many
        RAMType.objects.create(type="SDRAM")
        RAMType.objects.create(type="EDO")

        # two ram speeds to test many to many
        RAMSpeed.objects.create(speed="4400 MHz")
        RAMSpeed.objects.create(speed="6400 MHz")

        # create ram object and establish relationships
        Motherboard.objects.create(motherboard_id=1,
        name="testMotherboardObject",
        motherboard_manufacturer=Manufacturer.objects.get(id=1),
        cpu_socket_type=CPUSocketType.objects.get(id=1),
        memory_slots=2,
        storage_form_factor=StorageFormFactor.objects.get(id=1),
        max_memory_capacity=64)

        # add many to many relationships
        testObject = Motherboard.objects.get(motherboard_id=1)
        testObject.supported_ram_types.add(1,2)
        testObject.supported_ram_speeds.add(1,2)

        ### create ram objects to test compatibility with motherboard ###
        # create objects necesary to create a ram object
        RAMType.objects.create(type="DDR4")
        RAMSpeed.objects.create(speed="3200MHz")
        RAMCapacity.objects.create(capacity="16GB")
        RAMNumberOfModules.objects.create(number_of_modules=2)

        # create ram object and establish relationships
        RAM.objects.create(ram_id=1,
        ram_type=RAMType.objects.get(id=3),
        ram_speed=RAMSpeed.objects.get(id=3),
        ram_capacity=RAMCapacity.objects.get(id=1),
        ram_number_of_modules=RAMNumberOfModules.objects.get(id=1))

        ### create cpu object to test compatibililty with motherboard ###
        


        ### create storage object to test compatibility with motherboard ###

    # testing the labels of the fields
    def test_Motherboard_mb_id_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("motherboard_id").verbose_name
        self.assertEqual(field_label, "motherboard id")

    def test_Motherboard_name_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_Motherboard_manufacturer_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("motherboard_manufacturer").verbose_name
        self.assertEqual(field_label, "motherboard manufacturer")

    def test_Motherboard_cpusocket_type_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("cpu_socket_type").verbose_name
        self.assertEqual(field_label, "cpu socket type")

    def test_Motherboard_memory_slots_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("memory_slots").verbose_name
        self.assertEqual(field_label, "memory slots")

    def test_Motherboard_storage_form_factor_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("storage_form_factor").verbose_name
        self.assertEqual(field_label, "storage form factor")

    def test_Motherboard_max_memory_capacity_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("max_memory_capacity").verbose_name
        self.assertEqual(field_label, "max memory capacity")

    def test_Motherboard_supported_ram_types_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("supported_ram_types").verbose_name
        self.assertEqual(field_label, "supported ram types")

    def test_Motherboard_supported_ram_speeds_field_label(self):
        testObject = Motherboard.objects.get(motherboard_id=1)
        field_label = testObject._meta.get_field("supported_ram_speeds").verbose_name
        self.assertEqual(field_label, "supported ram speeds")