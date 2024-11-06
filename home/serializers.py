from rest_framework import serializers
from .models import *

#---------------------------------------------------------------------------------
# | Serializers for models that support CPU, Build, RAM, Storage, and MotherBoard |
#---------------------------------------------------------------------------------

#serializers to support cpu
class Manufacturerserializer(serializers.ModelSerializer):
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

# serializers to support rams
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

# serializers to support storages
class StorageFormFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageFormFactor
        exclude = ['id'] 
class StorageCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCapacity
        exclude = ['id']
class StorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        exclude = ['id']

class MotherBoardSerializer(serializers.ModelSerializer):
    motherboard_manufacturer = Manufacturerserializer()
    cpu_socket_type = CPUSocketTypeSerializer()
    storage_form_factor = StorageFormFactorSerializer()
    supported_ram_types = RAMTypeSerializer(many=True, read_only=True)
    supported_ram_speeds = RAMSpeedSerializer(many=True, read_only=True)

    class Meta:
        model = Motherboard
        fields = ('motherboard_id','name','motherboard_manufacturer','cpu_socket_type','memory_slots','storage_form_factor',
        'max_memory_capacity','supported_ram_types','supported_ram_speeds')

class CPUSerializer(serializers.ModelSerializer):
    cpu_manufacturer = Manufacturerserializer()
    cpu_microarchitecture = MicroarchitectureSerializer()
    socket_type = CPUSocketTypeSerializer()
    class Meta:
        model = CPU
        fields = ('cpu_id','cpu_name','cpu_manufacturer','cpu_microarchitecture','socket_type')

class RAMSerializer(serializers.ModelSerializer):
    ram_type = RAMTypeSerializer()
    ram_speed = RAMSpeedSerializer()
    ram_capacity = RAMCapacitySerializer()
    ram_number_of_modules = RAMNumberOfModulesSerializer()

    class Meta:
        model = RAM
        fields = ('ram_id','ram_type','ram_speed','ram_capacity','ram_number_of_modules')
    
class StorageSerializer(serializers.ModelSerializer):
    storage_form_factor = StorageFormFactorSerializer()
    storage_capacity = StorageCapacitySerializer()
    storage_type = StorageTypeSerializer()

    class Meta:
        model = Storage
        fields = ('storage_id','name','storage_form_factor','storage_capacity','storage_type')

# build model serializer
class BuildSerializer(serializers.ModelSerializer):
    motherboard = MotherBoardSerializer()
    cpu = CPUSerializer()
    ram = RAMSerializer(many=True, read_only=True)
    storage = StorageSerializer()

    class Meta:
        model = Build
        fields = ('build_id','name','profile','is_complete','motherboard',
        'cpu','ram','storage')

    def validate(self, data):
        motherboard = data.get('motherboard')
        cpu = data.get('cpu')
        ram = data.get('ram')

        if motherboard and cpu:
            if not motherboard.is_cpu_compatible(cpu):
                raise serializers.ValidationError("The selected CPU is not compatible with the motherboard.")

        if motherboard and ram:
            for ram_module in ram:
                if not motherboard.is_ram_compatible(ram_module):
                    raise serializers.ValidationError("The selected RAM is not compatible with the motherboard.")

        return data