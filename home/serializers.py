from rest_framework import serializers
from .models import Build

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
