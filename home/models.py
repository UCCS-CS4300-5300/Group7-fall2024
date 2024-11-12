from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    profile_name = models.CharField(max_length=20, blank=True)  # Optional profile name
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        indexes = [ 
            models.Index(fields=['profile_name'])  # Index the profile_name field for faster search 
        ]

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)  # Automatically create a profile when a user signs up

# Shopping cart model linked to a Profile
class Shopping_Cart(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # One-to-one relationship with the Profile model
    total_price = models.FloatField(default=0.0)  # Default total price for the shopping cart
    
    def __str__(self):
        return self.profile.profile_name  # String representation of the Shopping_Cart model

# Build Models
class Build(models.Model):
    """
    Build model containing the configuration of PC components.
    """
    build_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Build model
    name = models.CharField(max_length=100, default='Default Build Name', unique=True)  # Ensure unique build name
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)  # Foreign key to the Profile model
    is_complete = models.BooleanField(default=False)  # Flag to indicate if the build is complete
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE, null=True)  # Foreign key to Motherboard model
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE, null=True)  # Foreign key to CPU model
    ram = models.ManyToManyField('RAM', through='BuildRAM', blank=True)  # Many-to-many relationship with RAM model
    storages = models.ManyToManyField('Storage', through='BuildStorageConfiguration', related_name='build_storages')  # Many-to-many relationship with Storage model

    def __str__(self):
        return self.name  # String representation of the Build model

    def clean(self):
        # Custom validation logic can be added here if needed
        pass

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(is_complete__in=[True, False]), name='is_complete_valid')
        ]
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster queries
        ]

class BuildRAM(models.Model):
    """
    Intermediate model for the many-to-many relationship between Build and RAM.
    Links a build to its RAM modules.
    """
    build = models.ForeignKey('Build', on_delete=models.CASCADE)  # Foreign key to Build model
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)  # Foreign key to RAM model

    def __str__(self):
        return f"{self.build.name} - {self.ram}"  # String representation of the BuildRAM model

# General models
class Manufacturer(models.Model):
    """
    Model to define the manufacturer of components.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the manufacturer name is unique

    def __str__(self):
        return self.name  # String representation of the Manufacturer model

    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class CPUSocketType(models.Model):
    """
    Model to define CPU socket types.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the socket type name is unique

    def __str__(self):
        return self.name  # String representation of the CPUSocketType model

    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class FormFactor(models.Model):
    """
    Model to define form factors, applicable to various components.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the form factor name is unique

    def __str__(self):
        return self.name  # String representation of the FormFactor model

    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class StorageType(models.Model):
    """
    Model to define storage types.
    """
    type = models.CharField(max_length=100, unique=True)  # Ensure the storage type name is unique

    def __str__(self):
        return self.type  # String representation of the StorageType model

    class Meta:
        indexes = [
            models.Index(fields=['type'])  # Index the type field for faster search
        ]

# Motherboard models
class MotherboardQuerySet(models.QuerySet):
    def by_ram_type(self, ram_type):
        return self.filter(ram__type=ram_type)

class MotherboardManager(models.Manager):
    def get_queryset(self):
        return MotherboardQuerySet(self.model, using=self._db)

    def by_ram_type(self, ram_type):
        return self.get_queryset().by_ram_type(ram_type)

class Motherboard(models.Model):
    """
    Model to define a motherboard with its characteristics.
    """
    motherboard_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Motherboard model
    name = models.CharField(max_length=100, unique=True)  # Ensure unique motherboard name
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    cpu_socket_type = models.ForeignKey('CPUSocketType', on_delete=models.CASCADE)  # Foreign key to CPUSocketType model
    memory_slots = models.IntegerField(
        choices=[(2, '2 Slots'), (4, '4 Slots')],
        validators=[MinValueValidator(1), MaxValueValidator(4)]  # Validate memory slots between 1 and 4
    )  # Integer field for number of memory slots
    form_factor = models.ForeignKey('FormFactor', on_delete=models.CASCADE)  # Foreign key to FormFactor model
    max_memory_capacity = models.IntegerField(default=128, validators=[MinValueValidator(1)])  # Ensure positive memory capacity
    supported_ram_types = models.ManyToManyField('RAMType')  # Many-to-many relationship with RAMType model
    supported_ram_speeds = models.ManyToManyField('RAMSpeed')  # Many-to-many relationship with RAMSpeed model
    supported_storage_types = models.ManyToManyField('StorageType', through='SupportedStorageConfiguration')  # Many-to-many relationship with StorageType model through SupportedStorageConfiguration
    rams = models.ManyToManyField('RAM', through='SupportedRAMConfiguration')  # Many-to-many relationship with RAM model through SupportedRAMConfiguration

    def __str__(self):
        return self.name  # String representation of the Motherboard model

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(max_memory_capacity__gte=0), name='max_memory_capacity_positive')
        ]
        indexes = [
            models.Index(fields=['name']),  # Index the name field for faster search
            models.Index(fields=['manufacturer']),  # Index the manufacturer field for faster search
            models.Index(fields=['cpu_socket_type']),  # Index the cpu_socket_type field for faster search
            models.Index(fields=['form_factor']),  # Index the form_factor field for faster search
        ]

# RAM Models
class RAMType(models.Model):
    """
    Model to define types of RAM (e.g., DDR4).
    """
    type = models.CharField(max_length=10, unique=True)  # Type of RAM (e.g., DDR4)

    def __str__(self):
        return self.type  # String representation of the RAMType model

    class Meta:
        indexes = [
            models.Index(fields=['type'])  # Index the type field for faster search
        ]

class RAMSpeed(models.Model):
    """
    Model to define RAM speeds (e.g., 3200MHz).
    """
    speed = models.PositiveIntegerField(
        validators=[MinValueValidator(800), MaxValueValidator(5000)]  # Validate speed between 800 and 5000 MHz
    )

    def __str__(self):
        return f"{self.speed} MHz"  # String representation of the RAMSpeed model

    class Meta:
        indexes = [
            models.Index(fields=['speed'])  # Index the speed field for faster search
        ]

class RAMCapacity(models.Model):
    capacity = models.CharField(max_length=10)

    def __str__(self):
        return self.capacity

class RAMNumberOfModules(models.Model):
    number_of_modules = models.IntegerField()

    def __str__(self):
        return str(self.number_of_modules)

class RAM(models.Model):
    ram_id = models.AutoField(primary_key=True)
    ram_type = models.ForeignKey(RAMType, on_delete=models.CASCADE)
    ram_speed = models.ForeignKey(RAMSpeed, on_delete=models.CASCADE)
    ram_capacity = models.ForeignKey(RAMCapacity, on_delete=models.CASCADE)
    ram_number_of_modules = models.ForeignKey(RAMNumberOfModules, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ram_type} {self.ram_speed} - {self.ram_number_of_modules} x {self.ram_capacity}"

# Motherboard models
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CPUSocketType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StorageFormFactor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Motherboard(models.Model):
    motherboard_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    motherboard_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    cpu_socket_type = models.ForeignKey(CPUSocketType, on_delete=models.CASCADE)
    memory_slots = models.IntegerField(choices=[(2, '2 Slots'), (4, '4 Slots')])
    storage_form_factor = models.ForeignKey(StorageFormFactor, on_delete=models.CASCADE)
    max_memory_capacity = models.IntegerField(default=128)
    supported_ram_types = models.ManyToManyField(RAMType)
    supported_ram_speeds = models.ManyToManyField(RAMSpeed)

    def __str__(self):
        return self.name

    # Compatibility checks for RAM
    def is_ram_type_compatible(self, ram):
        return ram.ram_type in self.supported_ram_types.all()

    def is_ram_speed_compatible(self, ram):
        return ram.ram_speed in self.supported_ram_speeds.all()

    def is_ram_capacity_compatible(self, ram):
        total_capacity = int(ram.ram_capacity.capacity.split()[0]) * ram.ram_number_of_modules.number_of_modules
        return total_capacity <= self.max_memory_capacity

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
        return f"{self.name} - {self.form_factor.name} - {self.capacity.capacity}"  # String representation of the Storage model

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Index the name field for faster search
            models.Index(fields=['manufacturer']),  # Index the manufacturer field for faster search
            models.Index(fields=['form_factor']),  # Index the form_factor field for faster search
            models.Index(fields=['type'])  # Index the type field for faster search
        ]

# Intermediary Models
class SupportedRAMConfiguration(models.Model):
    """
    Intermediate model for the many-to-many relationship between Motherboard and RAM.
    Stores whether a specific RAM module is supported by a specific motherboard.
    """
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE)  # Foreign key to Motherboard model
    ram = models.ForeignKey('RAM', on_delete=models.CASCADE)  # Foreign key to RAM model
    supported = models.BooleanField(default=True)  # Boolean field indicating support status

    def __str__(self):
        return f"{self.motherboard.name} supports {self.ram}"  # String representation of the model

    class Meta:
        unique_together = ('motherboard', 'ram')  # Ensure unique combinations of motherboard and RAM
        constraints = [
            models.CheckConstraint(check=models.Q(supported__in=[True, False]), name='supported_valid')
        ]
        indexes = [
            models.Index(fields=['motherboard']),  # Index the motherboard field for faster search
            models.Index(fields=['ram']),  # Index the ram field for faster search
        ]

class SupportedStorageConfiguration(models.Model):
    """
    Intermediate model for the many-to-many relationship between Motherboard and StorageType.
    Stores the number of slots available for a specific storage type on a specific motherboard.
    """
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE)  # Foreign key to Motherboard model
    storage_type = models.ForeignKey('StorageType', on_delete=models.CASCADE)  # Foreign key to StorageType model
    slots = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Integer field for the number of slots available

    def __str__(self):
        return f"{self.motherboard.name} supports {self.storage_type.type} with {self.slots} slots"  # String representation of the model

    class Meta:
        unique_together = ('motherboard', 'storage_type')  # Ensure unique combinations of motherboard and storage type
        constraints = [
            models.CheckConstraint(check=models.Q(slots__gte=0), name='slots_positive')
        ]
        indexes = [
            models.Index(fields=['motherboard']),  # Index the motherboard field for faster search
            models.Index(fields=['storage_type']),  # Index the storage_type field for faster search
        ]

class CPUMotherboardCompatibility(models.Model):
    """
    Intermediate model for the many-to-many relationship between CPU and Motherboard.
    """
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE)  # Foreign key to CPU model
    motherboard = models.ForeignKey('Motherboard', on_delete=models.CASCADE)  # Foreign key to Motherboard model

    def __str__(self):
        return f"{self.cpu.name} is compatible with {self.motherboard.name}"  # String representation of the model

    class Meta:
        unique_together = ('cpu', 'motherboard')  # Ensure unique combinations of CPU and motherboard
        indexes = [
            models.Index(fields=['cpu']),  # Index the cpu field for faster search
            models.Index(fields=['motherboard']),  # Index the motherboard field for faster search
        ]

class BuildStorageConfiguration(models.Model):
    """
    Intermediate model for the many-to-many relationship between Build and Storage.
    Stores the role (e.g., primary, secondary) of a specific storage device within a specific build.
    """
    build = models.ForeignKey('Build', on_delete=models.CASCADE)  # Foreign key to Build model
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)  # Foreign key to Storage model
    role = models.CharField(max_length=50, default='Secondary')  # Role of the storage device within the build

    def __str__(self):
        return f"{self.build.name} - {self.storage.name} ({self.role})"  # String representation of the model

    class Meta:
        unique_together = ('build', 'storage')  # Ensure unique combinations of build and storage
        constraints = [
            models.CheckConstraint(check=models.Q(role__in=['Primary', 'Secondary']), name='role_valid')
        ]
        indexes = [
            models.Index(fields=['build']),  # Index the build field for faster search
            models.Index(fields=['storage']),  # Index the storage field for faster search
        ]
