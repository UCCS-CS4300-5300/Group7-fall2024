from rest_framework import serializers
from .models import Build, Motherboard, CPU, RAM, Storage

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
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
