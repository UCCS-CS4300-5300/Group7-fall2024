from rest_framework import serializers
from .models import *
from .compatibility_service import CompatibilityService

# Serializers for core models

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ['id']

class MicroarchitectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microarchitecture
        exclude = ['id']

class CPUSocketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUSocketType
        exclude = ['id']

# RAM Serializers
class RAMTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAMType
        fields = '__all__'

class RAMSpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAMSpeed
        fields = '__all__'

class RAMCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RAMCapacity
        exclude = ['id']

class RAMNumberOfModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAMNumberOfModules
        exclude = ['id']

# Storage Serializers
class FormFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFactor
        exclude = ['id']

class StorageCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCapacity
        exclude = ['id']

class StorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        exclude = ['id']

class MotherboardSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    cpu_socket_type = CPUSocketTypeSerializer()
    form_factor = FormFactorSerializer()
    supported_ram_types = RAMTypeSerializer(many=True, read_only=True)
    supported_ram_speeds = RAMSpeedSerializer(many=True, read_only=True)

    class Meta:
        model = Motherboard
        fields = (
            'motherboard_id', 'name', 'manufacturer', 'cpu_socket_type', 'memory_slots', 'form_factor',
            'max_memory_capacity', 'supported_ram_types', 'supported_ram_speeds'
        )

class CPUSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    microarchitecture = MicroarchitectureSerializer()
    socket_type = CPUSocketTypeSerializer()
    
    class Meta:
        model = CPU
        fields = ('cpu_id', 'name', 'manufacturer', 'microarchitecture', 'socket_type')

class RAMSerializer(serializers.ModelSerializer):
    ram_type = RAMTypeSerializer()
    ram_speed = RAMSpeedSerializer()
    ram_capacity = RAMCapacitySerializer()
    ram_number_of_modules = RAMNumberOfModulesSerializer()

    class Meta:
        model = RAM
        fields = ('ram_id', 'name', 'manufacturer', 'ram_type', 'ram_speed', 'ram_capacity', 'ram_number_of_modules')

class StorageSerializer(serializers.ModelSerializer):
    form_factor = FormFactorSerializer()
    capacity = StorageCapacitySerializer()
    type = StorageTypeSerializer()

    class Meta:
        model = Storage
        fields = ('storage_id', 'name', 'manufacturer', 'form_factor', 'capacity', 'type')

# Build Serializer
class BuildSerializer(serializers.ModelSerializer):
    motherboard = MotherboardSerializer()
    cpu = CPUSerializer()
    ram = RAMSerializer(many=True, read_only=True)
    storage = StorageSerializer(many=True, read_only=True)

    class Meta:
        model = Build
        fields = ('build_id', 'name', 'profile', 'is_complete', 'motherboard', 'cpu', 'ram', 'storage')

    def validate(self, data):
        """
        Validate the build by checking component compatibility using the CompatibilityService.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data if no issues are found.

        Raises:
            serializers.ValidationError: If any compatibility issues are found.
        """
        build = self.instance or Build(**data)
        compatible, issues = CompatibilityService.check_build_compatibility(build)
        
        if not compatible:
            raise serializers.ValidationError(issues)

        return data
