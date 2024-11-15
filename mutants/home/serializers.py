
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


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

    def xǁBuildSerializerǁvalidate__mutmut_orig(self, data):
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

    def xǁBuildSerializerǁvalidate__mutmut_1(self, data):
        """
        Validate the build by checking component compatibility using the CompatibilityService.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data if no issues are found.

        Raises:
            serializers.ValidationError: If any compatibility issues are found.
        """
        build = self.instance and Build(**data)
        compatible, issues = CompatibilityService.check_build_compatibility(build)
        
        if not compatible:
            raise serializers.ValidationError(issues)

        return data

    def xǁBuildSerializerǁvalidate__mutmut_2(self, data):
        """
        Validate the build by checking component compatibility using the CompatibilityService.

        Args:
            data (dict): The data to be validated.

        Returns:
            dict: The validated data if no issues are found.

        Raises:
            serializers.ValidationError: If any compatibility issues are found.
        """
        build = None
        compatible, issues = CompatibilityService.check_build_compatibility(build)
        
        if not compatible:
            raise serializers.ValidationError(issues)

        return data

    def xǁBuildSerializerǁvalidate__mutmut_3(self, data):
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
        compatible, issues = CompatibilityService.check_build_compatibility(None)
        
        if not compatible:
            raise serializers.ValidationError(issues)

        return data

    def xǁBuildSerializerǁvalidate__mutmut_4(self, data):
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
        compatible, issues = None
        
        if not compatible:
            raise serializers.ValidationError(issues)

        return data

    def xǁBuildSerializerǁvalidate__mutmut_5(self, data):
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
        
        if  compatible:
            raise serializers.ValidationError(issues)

        return data

    def xǁBuildSerializerǁvalidate__mutmut_6(self, data):
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
            raise serializers.ValidationError(None)

        return data

    xǁBuildSerializerǁvalidate__mutmut_mutants = {
    'xǁBuildSerializerǁvalidate__mutmut_1': xǁBuildSerializerǁvalidate__mutmut_1, 
        'xǁBuildSerializerǁvalidate__mutmut_2': xǁBuildSerializerǁvalidate__mutmut_2, 
        'xǁBuildSerializerǁvalidate__mutmut_3': xǁBuildSerializerǁvalidate__mutmut_3, 
        'xǁBuildSerializerǁvalidate__mutmut_4': xǁBuildSerializerǁvalidate__mutmut_4, 
        'xǁBuildSerializerǁvalidate__mutmut_5': xǁBuildSerializerǁvalidate__mutmut_5, 
        'xǁBuildSerializerǁvalidate__mutmut_6': xǁBuildSerializerǁvalidate__mutmut_6
    }

    def validate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildSerializerǁvalidate__mutmut_orig"), object.__getattribute__(self, "xǁBuildSerializerǁvalidate__mutmut_mutants"), *args, **kwargs)
        return result 

    validate.__signature__ = _mutmut_signature(xǁBuildSerializerǁvalidate__mutmut_orig)
    xǁBuildSerializerǁvalidate__mutmut_orig.__name__ = 'xǁBuildSerializerǁvalidate'


