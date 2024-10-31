from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re

# Profile model to extend the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    profile_name = models.CharField(max_length=20, blank=True)  # Optional profile name
    
    def __str__(self):
        return self.user.username  # String representation of the Profile model

# Signal to create a user Profile by default when a user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)  # Automatically create a profile when a user signs up

# Shopping cart model linked to a Profile
class Shopping_Cart(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # One-to-one relationship with the Profile model
    total_price = models.FloatField(default=0.0)  # Default total price for the shopping cart
    
    def __str__(self):
        return self.profile.profile_name  # String representation of the Shopping_Cart model

# Container model for the parts of the PC build
class Build(models.Model):
    build_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Build model
    name = models.CharField(max_length=100, default='Default Build Name')  # Name of the build
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Foreign key to the Profile model
    is_complete = models.BooleanField(default=False)  # Flag to indicate if the build is complete
    motherboard = models.ForeignKey('MotherBoard', on_delete=models.CASCADE, null=True)  # Foreign key to MotherBoard model
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE, null=True)  # Foreign key to CPU model
    ram = models.ManyToManyField('RAM', through='BuildRAM', blank=True)  # Many-to-many relationship with RAM model
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE, null=True)  # Foreign key to Storage model

    # Override save method to check compatibility
    def save(self, *args, **kwargs):
        if self.motherboard and self.cpu:
            if not self.motherboard.is_cpu_compatible(self.cpu):
                raise ValueError("The selected CPU is not compatible with the motherboard.")
        super(Build, self).save(*args, **kwargs)
        if self.motherboard and self.ram.exists():
            for ram_module in self.ram.all():
                if not self.motherboard.is_ram_compatible(ram_module):
                    raise ValueError("The selected RAM is not compatible with the motherboard.")
        super(Build, self).save(*args, **kwargs)

# Through model for Build and RAM relationship
class BuildRAM(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)  # Foreign key to Build model
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)  # Foreign key to RAM model

# Memory models
class RAMType(models.Model):
    type = models.CharField(max_length=10)  # Type of RAM (e.g., DDR4)
    
    def __str__(self):
        return self.type  # String representation of the RAMType model

class RAMSpeed(models.Model):
    speed = models.CharField(max_length=10)  # Speed of RAM (e.g., 3200MHz)
    
    def __str__(self):
        return self.speed  # String representation of the RAMSpeed model

class RAMCapacity(models.Model):
    capacity = models.CharField(max_length=10)  # Capacity of RAM (e.g., 16GB)
    
    def __str__(self):
        return self.capacity  # String representation of the RAMCapacity model

class RAMNumberOfModules(models.Model):
    number_of_modules = models.IntegerField()  # Number of RAM modules
    
    def __str__(self):
        return str(self.number_of_modules)  # String representation of the RAMNumberOfModules model

class RAM(models.Model):
    ram_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for RAM model
    ram_type = models.ForeignKey(RAMType, on_delete=models.CASCADE)  # Foreign key to RAMType model
    ram_speed = models.ForeignKey(RAMSpeed, on_delete=models.CASCADE)  # Foreign key to RAMSpeed model
    ram_capacity = models.ForeignKey(RAMCapacity, on_delete=models.CASCADE)  # Foreign key to RAMCapacity model
    ram_number_of_modules = models.ForeignKey(RAMNumberOfModules, on_delete=models.CASCADE)  # Foreign key to RAMNumberOfModules model
    
    def __str__(self):
        return f"{self.ram_type} {self.ram_speed} - {self.ram_number_of_modules} x {self.ram_capacity}"  # String representation of the RAM model

# Motherboard models
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)  # Name of the manufacturer
    
    def __str__(self):
        return self.name  # String representation of the Manufacturer model

class CPUSocketType(models.Model):
    name = models.CharField(max_length=100)  # Type of CPU socket
    
    def __str__(self):
        return self.name  # String representation of the CPUSocketType model

class StorageFormFactor(models.Model):
    name = models.CharField(max_length=100)  # Form factor of storage (e.g., 2.5", M.2)
    
    def __str__(self):
        return self.name  # String representation of the StorageFormFactor model

class Motherboard(models.Model):
    motherboard_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Motherboard model
    name = models.CharField(max_length=100)  # Name of the motherboard
    motherboard_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    cpu_socket_type = models.ForeignKey(CPUSocketType, on_delete=models.CASCADE)  # Foreign key to CPUSocketType model
    memory_slots = models.IntegerField(choices=[(2, '2 Slots'), (4, '4 Slots')])  # Number of memory slots
    storage_form_factor = models.ForeignKey(StorageFormFactor, on_delete=models.CASCADE)  # Foreign key to StorageFormFactor model
    max_memory_capacity = models.IntegerField(default=128)  # Maximum memory capacity supported
    supported_ram_types = models.ManyToManyField(RAMType)  # Many-to-many relationship with RAMType
    supported_ram_speeds = models.ManyToManyField(RAMSpeed)  # Many-to-many relationship with RAMSpeed
    
    def __str__(self):
        return self.name  # String representation of the Motherboard model

    # Compatibility checks for RAM
    def is_ram_type_compatible(self, ram):
        return ram.ram_type in self.supported_ram_types.all()
    
    def is_ram_speed_compatible(self, ram):
        return ram.ram_speed in self.supported_ram_speeds.all()
    
    def is_ram_capacity_compatible(self, ram):
        try:
            # Extract numeric part from the capacity string
            total_capacity = int(re.match(r'\d+', ram.ram_capacity.capacity).group()) * ram.ram_number_of_modules.number_of_modules
            return total_capacity <= self.max_memory_capacity
        except (ValueError, AttributeError):
            return False

    def is_ram_modules_compatible(self, ram):
        return ram.ram_number_of_modules.number_of_modules <= self.memory_slots
    
    def is_ram_compatible(self, ram):
        return (self.is_ram_type_compatible(ram) and self.is_ram_speed_compatible(ram) and self.is_ram_capacity_compatible(ram) and self.is_ram_modules_compatible(ram))

    # Compatibility check for CPU
    def is_cpu_compatible(self, cpu):
        return self.cpu_socket_type == cpu.socket_type

    # Compatibility check for storage
    def is_storage_compatible(self, storage):
        return self.storage_form_factor == storage.storage_form_factor
    
    # Overall build compatibility check
    def is_build_compatible(self, cpu, ram, storage):
        return (self.is_cpu_compatible(cpu) and self.is_ram_compatible(ram) and self.is_storage_compatible(storage))

# CPU models
class Microarchitecture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CPU(models.Model):
    cpu_id = models.AutoField(primary_key=True)
    cpu_name = models.CharField(max_length=100)
    cpu_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    cpu_microarchitecture = models.ForeignKey(Microarchitecture, on_delete=models.CASCADE)
    socket_type = models.ForeignKey(CPUSocketType, on_delete=models.CASCADE)

    def __str__(self):
        return self.cpu_name

# Storage models
class StorageCapacity(models.Model):
    capacity = models.CharField(max_length=100)

    def __str__(self):
        return self.capacity

class StorageType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    storage_form_factor = models.ForeignKey(StorageFormFactor, on_delete=models.CASCADE)
    storage_capacity = models.ForeignKey(StorageCapacity, on_delete=models.CASCADE)
    storage_type = models.ForeignKey(StorageType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.storage_form_factor.name} - {self.storage_capacity.capacity}"
