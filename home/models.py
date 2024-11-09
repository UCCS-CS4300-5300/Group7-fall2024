from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Profile model to extend the User model
class Profile(models.Model):
    """
    Profile model to extend the User model with a profile name.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    profile_name = models.CharField(max_length=20, blank=True)  # Optional profile name
    
    def __str__(self):
        return self.user.username  # String representation of the Profile model

# Signal to create a user Profile by default when a user signs up
def create_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile instance when a User is created.
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)  # Automatically create a profile when a user signs up

# Shopping cart model linked to a Profile
class ShoppingCart(models.Model):
    """
    ShoppingCart model linked to a Profile, tracking the total price of items.
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # One-to-one relationship with the Profile model
    total_price = models.FloatField(default=0.0)  # Default total price for the shopping cart
    
    def __str__(self):
        return self.profile.profile_name  # String representation of the ShoppingCart model

# Container model for the parts of the PC build
class Build(models.Model):
    """
    Build model containing the configuration of PC components.
    """
    build_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Build model
    name = models.CharField(max_length=100, default='Default Build Name')  # Name of the build
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  # Foreign key to the Profile model
    is_complete = models.BooleanField(default=False)  # Flag to indicate if the build is complete
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE, null=True)  # Foreign key to Motherboard model
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE, null=True)  # Foreign key to CPU model
    ram = models.ManyToManyField('RAM', through='BuildRAM', blank=True)  # Many-to-many relationship with RAM model
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE, null=True)  # Foreign key to Storage model

    def __str__(self):
        return self.name  # String representation of the Build model

# Through model for Build and RAM relationship
class BuildRAM(models.Model):
    """
    Intermediate model for the many-to-many relationship between Build and RAM.
    """
    build = models.ForeignKey(Build, on_delete=models.CASCADE)  # Foreign key to Build model
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)  # Foreign key to RAM model

    def __str__(self):
        return f"{self.build.name} - {self.ram}"  # String representation of the BuildRAM model

# RAM models# Memory models
class RAMType(models.Model):
    """
    Model to define types of RAM (e.g., DDR4).
    """
    type = models.CharField(max_length=10)  # Type of RAM (e.g., DDR4)
    
    def __str__(self):
        return self.type  # String representation of the RAMType model

class RAMSpeed(models.Model):
    """
    Model to define RAM speeds (e.g., 3200MHz).
    """
    speed = models.CharField(max_length=10)  # Speed of RAM (e.g., 3200MHz)
    
    def __str__(self):
        return self.speed  # String representation of the RAMSpeed model

class RAMCapacity(models.Model):
    """
    Model to define RAM capacity (e.g., 16GB).
    """
    capacity = models.CharField(max_length=10)  # Capacity of RAM (e.g., 16GB)
    
    def __str__(self):
        return self.capacity  # String representation of the RAMCapacity model

class RAMNumberOfModules(models.Model):
    """
    Model to define the number of RAM modules.
    """
    number_of_modules = models.IntegerField()  # Number of RAM modules
    
    def __str__(self):
        return str(self.number_of_modules)  # String representation of the RAMNumberOfModules model

class RAM(models.Model):
    """
    Model to define a RAM component with its characteristics.
    """
    ram_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for RAM model
    ram_type = models.ForeignKey(RAMType, on_delete=models.CASCADE)  # Foreign key to RAMType model
    ram_speed = models.ForeignKey(RAMSpeed, on_delete=models.CASCADE)  # Foreign key to RAMSpeed model
    ram_capacity = models.ForeignKey(RAMCapacity, on_delete=models.CASCADE)  # Foreign key to RAMCapacity model
    ram_number_of_modules = models.ForeignKey(RAMNumberOfModules, on_delete=models.CASCADE)  # Foreign key to RAMNumberOfModules model
    
    def __str__(self):
        return f"{self.ram_type} {self.ram_speed} - {self.ram_number_of_modules} x {self.ram_capacity}"  # String representation of the RAM model

# Motherboard models
class Manufacturer(models.Model):
    """
    Model to define the manufacturer of components.
    """
    name = models.CharField(max_length=100)  # Name of the manufacturer
    
    def __str__(self):
        return self.name  # String representation of the Manufacturer model

class CPUSocketType(models.Model):
    """
    Model to define CPU socket types.
    """
    name = models.CharField(max_length=100)  # Type of CPU socket
    
    def __str__(self):
        return self.name  # String representation of the CPUSocketType model

class StorageFormFactor(models.Model):
    """
    Model to define storage form factors (e.g., 2.5", M.2).
    """
    name = models.CharField(max_length=100)  # Form factor of storage (e.g., 2.5", M.2)
    
    def __str__(self):
        return self.name  # String representation of the StorageFormFactor model

class StorageType(models.Model):
    """
    Model to define storage type.
    """
    type = models.CharField(max_length=100)  # Type of storage (e.g., SSD, HDD)

    def __str__(self):
        return self.type  # String representation of the StorageType model

class Motherboard(models.Model):
    """
    Model to define a motherboard with its characteristics.
    """
    motherboard_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Motherboard model
    name = models.CharField(max_length=100)  # Name of the motherboard
    motherboard_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    cpu_socket_type = models.ForeignKey(CPUSocketType, on_delete=models.CASCADE)  # Foreign key to CPUSocketType model
    memory_slots = models.IntegerField(choices=[(2, '2 Slots'), (4, '4 Slots')])  # Number of memory slots
    storage_form_factor = models.ManyToManyField(StorageFormFactor)  # Foreign key to StorageFormFactor model
    max_memory_capacity = models.IntegerField(default=128)  # Maximum memory capacity supported
    supported_ram_types = models.ManyToManyField(RAMType)  # Many-to-many relationship with RAMType
    supported_ram_speeds = models.ManyToManyField(RAMSpeed)  # Many-to-many relationship with RAMSpeed
    supported_storage_types = models.ManyToManyField(StorageType)  # Many-to-many relationship with StorageType

    def __str__(self):
        return self.name  # String representation of the Motherboard model

# CPU models
class Microarchitecture(models.Model):
    """
    Model to define CPU microarchitecture.
    """
    name = models.CharField(max_length=100)  # Name of the microarchitecture

    def __str__(self):
        return self.name  # String representation of the Microarchitecture model

class CPU(models.Model):
    """
    Model to define a CPU with its characteristics.
    """
    cpu_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for CPU model
    cpu_name = models.CharField(max_length=100)  # Name of the CPU
    cpu_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    cpu_microarchitecture = models.ForeignKey(Microarchitecture, on_delete=models.CASCADE)  # Foreign key to Microarchitecture model
    socket_type = models.ForeignKey(CPUSocketType, on_delete=models.CASCADE)  # Foreign key to CPUSocketType model

    def __str__(self):
        return self.cpu_name  # String representation of the CPU model

# Storage models
class StorageCapacity(models.Model):
    """
    Model to define storage capacity.
    """
    capacity = models.CharField(max_length=100)  # Capacity of storage (e.g., 1TB)

    def __str__(self):
        return self.capacity  # String representation of the StorageCapacity model

class Storage(models.Model):
    """
    Model to define a storage component with its characteristics.
    """
    storage_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for storage model
    name = models.CharField(max_length=100)  # Name of the storage device
    storage_form_factor = models.ForeignKey(StorageFormFactor, on_delete=models.CASCADE)  # Foreign key to StorageFormFactor model
    storage_capacity = models.ForeignKey(StorageCapacity, on_delete=models.CASCADE)  # Foreign key to StorageCapacity model
    storage_type = models.ForeignKey(StorageType, on_delete=models.CASCADE)  # Foreign key to StorageType model

    def __str__(self):
        return f"{self.name} - {self.storage_form_factor.name} - {self.storage_capacity.capacity}"  # String representation of the Storage model
