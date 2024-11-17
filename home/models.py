from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=20, blank=True)
    
    current_build = models.OneToOneField(
        'Build', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='active_profile'
    )

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

class ShoppingCart(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"Shopping Cart for {self.profile.user.username}"

# Build Models
class Build(models.Model):
    """
    Build model containing the configuration of PC components.
    """
    build_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for Build model
    name = models.CharField(max_length=100, default='Default Build Name')  # Ensure unique build name
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)  # Foreign key to the Profile model
    is_complete = models.BooleanField(default=False)  # Flag to indicate if the build is complete
    is_active = models.BooleanField(default=False)
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
            models.CheckConstraint(condition=models.Q(is_complete__in=[True, False]), name='is_complete_valid'),
            models.CheckConstraint(condition=models.Q(is_active__in=[True, False]), name='is_active_valid'),  # NEW: Ensure is_active is valid

        ]
        indexes = [
            models.Index(fields=['name']),  # Index the name field for faster queries
            models.Index(fields=['is_active']),  # NEW: Index is_active for faster queries

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
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Price of the Motherboard
    image = models.ImageField(upload_to='images/motherboard/', null=True, blank=True)  # Image of the Motherboard
    description = models.TextField(blank=True)  # Add description field here

    def __str__(self):
        return self.name  # String representation of the Motherboard model

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(max_memory_capacity__gte=0), name='max_memory_capacity_positive')
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
    """
    Model to define RAM capacity (e.g., 16GB).
    """
    capacity = models.CharField(max_length=10)

    def __str__(self):
        return self.capacity  # String representation of the RAMCapacity model

    class Meta:
        indexes = [
            models.Index(fields=['capacity'])  # Index the capacity field for faster search
        ]

class RAMNumberOfModules(models.Model):
    """
    Model to define the number of RAM modules.
    """
    number_of_modules = models.IntegerField(validators=[MinValueValidator(1)])  # Ensure at least 1 module

    def __str__(self):
        return str(self.number_of_modules)  # String representation of the RAMNumberOfModules model

    class Meta:
        indexes = [
            models.Index(fields=['number_of_modules'])  # Index the number_of_modules field for faster search
        ]

class RAMManager(models.Manager):
    def by_type(self, ram_type):
        return self.filter(ram_type__type=ram_type)

    def by_speed_range(self, min_speed, max_speed):
        return self.filter(ram_speed__speed__gte=min_speed, ram_speed__speed__lte=max_speed)

class RAM(models.Model):
    """
    Model to define a RAM component with its characteristics.
    """
    ram_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for RAM model
    name = models.CharField(max_length=100)  # Name of the RAM component
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    ram_type = models.ForeignKey('RAMType', on_delete=models.CASCADE)  # Foreign key to RAMType model
    ram_speed = models.ForeignKey('RAMSpeed', on_delete=models.CASCADE)  # Foreign key to RAMSpeed model
    ram_capacity = models.ForeignKey('RAMCapacity', on_delete=models.CASCADE)  # Foreign key to RAMCapacity model
    ram_number_of_modules = models.ForeignKey('RAMNumberOfModules', on_delete=models.CASCADE)  # Foreign key to RAMNumberOfModules model
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Price of the RAM
    image = models.ImageField(upload_to='images/ram/', null=True, blank=True)  # Image of the RAM
    description = models.TextField(blank=True)  # Add description field here

    def clean(self):
        # Custom validation logic
        if self.ram_speed.speed not in range(800, 8001):
            raise ValidationError(f"RAM speed {self.ram_speed.speed} is out of the valid range.")

    def __str__(self):
        return f"{self.name} {self.ram_type.type} {self.ram_speed.speed} MHz - {self.ram_number_of_modules.number_of_modules} x {self.ram_capacity.capacity}"  # Improved string representation

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Index the name field for faster search
            models.Index(fields=['manufacturer']),  # Index the manufacturer field for faster search
        ]

# CPU Models
class Microarchitecture(models.Model):
    """
    Model to define CPU microarchitecture.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the microarchitecture name is unique

    def __str__(self):
        return self.name  # String representation of the Microarchitecture model

    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class CPUMicroarchitectureManager(models.Manager):
    def by_microarchitecture(self, name):
        return self.filter(microarchitecture__name=name)

    def by_socket_type(self, socket_type_name):
        return self.filter(socket_type__name=socket_type_name)

class CPU(models.Model):
    """
    Model to define a CPU with its characteristics.
    """
    cpu_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for CPU model
    name = models.CharField(max_length=100, unique=True)  # Ensure unique CPU name
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    microarchitecture = models.ForeignKey('Microarchitecture', on_delete=models.CASCADE)  # Foreign key to Microarchitecture model
    socket_type = models.ForeignKey('CPUSocketType', on_delete=models.CASCADE)  # Foreign key to CPUSocketType model
    motherboards = models.ManyToManyField('Motherboard', through='CPUMotherboardCompatibility')  # Many-to-Many relationship with Motherboard
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Price of the CPU
    image = models.ImageField(upload_to='images/cpu/', null=True, blank=True)  # Image of the CPU
    description = models.TextField(blank=True)  # Add description field here

    objects = CPUMicroarchitectureManager()  # Use custom manager

    def __str__(self):
        return self.name  # String representation of the CPU model

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Index the name field for faster search
            models.Index(fields=['manufacturer']),  # Index the manufacturer field for faster search
            models.Index(fields=['microarchitecture']),  # Index the microarchitecture field for faster search
            models.Index(fields=['socket_type'])  # Index the socket_type field for faster search
        ]

# Storage Models
class StorageCapacity(models.Model):
    """
    Model to define storage capacity.
    """
    capacity = models.CharField(max_length=100, unique=True)  # Ensure the storage capacity is unique

    def __str__(self):
        return self.capacity  # String representation of the StorageCapacity model

    class Meta:
        indexes = [
            models.Index(fields=['capacity'])  # Index the capacity field for faster search
        ]

class StorageManager(models.Manager):
    def by_type(self, storage_type):
        return self.filter(type__type=storage_type)

    def by_capacity_range(self, min_capacity, max_capacity):
        return self.filter(capacity__capacity__gte=min_capacity, capacity__capacity__lte=max_capacity)

class Storage(models.Model):
    """
    Model to define a storage component with its characteristics.
    """
    storage_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key for storage model
    name = models.CharField(max_length=100)  # Name of the storage device
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)  # Foreign key to Manufacturer model
    form_factor = models.ForeignKey('FormFactor', on_delete=models.CASCADE)  # Foreign key to FormFactor model
    capacity = models.ForeignKey('StorageCapacity', on_delete=models.CASCADE)  # Foreign key to StorageCapacity model
    type = models.ForeignKey('StorageType', on_delete=models.CASCADE)  # Foreign key to StorageType model
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Price of the Storage
    image = models.ImageField(upload_to='images/storage/', null=True, blank=True)  # Image of the Storage
    description = models.TextField(blank=True)  # Add description field here

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
            models.CheckConstraint(condition=models.Q(supported__in=[True, False]), name='supported_valid')
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
            models.CheckConstraint(condition=models.Q(slots__gte=0), name='slots_positive')
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
            models.CheckConstraint(condition=models.Q(role__in=['Primary', 'Secondary']), name='role_valid')
        ]
        indexes = [
            models.Index(fields=['build']),  # Index the build field for faster search
            models.Index(fields=['storage']),  # Index the storage field for faster search
        ]
