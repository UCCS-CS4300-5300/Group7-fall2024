from rest_framework import serializers
from .models import *

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'

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

class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'

class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


# once all of the serializers are created, we can nest them so that the
# pk's arent shown and the actual records/objects are shown in output.