
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


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=20, blank=True)
    
    def xǁProfileǁ__str____mutmut_orig(self):
        return self.user.username

    xǁProfileǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProfileǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁProfileǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁProfileǁ__str____mutmut_orig)
    xǁProfileǁ__str____mutmut_orig.__name__ = 'xǁProfileǁ__str__'


    
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
    
    def xǁShoppingCartǁ__str____mutmut_orig(self):
        return f"Shopping Cart for {self.profile.user.username}"

    xǁShoppingCartǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁShoppingCartǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁShoppingCartǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁShoppingCartǁ__str____mutmut_orig)
    xǁShoppingCartǁ__str____mutmut_orig.__name__ = 'xǁShoppingCartǁ__str__'



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

    def xǁBuildǁ__str____mutmut_orig(self):
        return self.name  # String representation of the Build model

    xǁBuildǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁBuildǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁBuildǁ__str____mutmut_orig)
    xǁBuildǁ__str____mutmut_orig.__name__ = 'xǁBuildǁ__str__'



    def xǁBuildǁclean__mutmut_orig(self):
        # Custom validation logic can be added here if needed
        pass

    xǁBuildǁclean__mutmut_mutants = {

    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildǁclean__mutmut_orig"), object.__getattribute__(self, "xǁBuildǁclean__mutmut_mutants"), *args, **kwargs)
        return result 

    clean.__signature__ = _mutmut_signature(xǁBuildǁclean__mutmut_orig)
    xǁBuildǁclean__mutmut_orig.__name__ = 'xǁBuildǁclean'



    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(is_complete__in=[True, False]), name='is_complete_valid')
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

    def xǁBuildRAMǁ__str____mutmut_orig(self):
        return f"{self.build.name} - {self.ram}"  # String representation of the BuildRAM model

    xǁBuildRAMǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildRAMǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁBuildRAMǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁBuildRAMǁ__str____mutmut_orig)
    xǁBuildRAMǁ__str____mutmut_orig.__name__ = 'xǁBuildRAMǁ__str__'



# General models
class Manufacturer(models.Model):
    """
    Model to define the manufacturer of components.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the manufacturer name is unique

    def xǁManufacturerǁ__str____mutmut_orig(self):
        return self.name  # String representation of the Manufacturer model

    xǁManufacturerǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁManufacturerǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁManufacturerǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁManufacturerǁ__str____mutmut_orig)
    xǁManufacturerǁ__str____mutmut_orig.__name__ = 'xǁManufacturerǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class CPUSocketType(models.Model):
    """
    Model to define CPU socket types.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the socket type name is unique

    def xǁCPUSocketTypeǁ__str____mutmut_orig(self):
        return self.name  # String representation of the CPUSocketType model

    xǁCPUSocketTypeǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCPUSocketTypeǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCPUSocketTypeǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCPUSocketTypeǁ__str____mutmut_orig)
    xǁCPUSocketTypeǁ__str____mutmut_orig.__name__ = 'xǁCPUSocketTypeǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class FormFactor(models.Model):
    """
    Model to define form factors, applicable to various components.
    """
    name = models.CharField(max_length=100, unique=True)  # Ensure the form factor name is unique

    def xǁFormFactorǁ__str____mutmut_orig(self):
        return self.name  # String representation of the FormFactor model

    xǁFormFactorǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFormFactorǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁFormFactorǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁFormFactorǁ__str____mutmut_orig)
    xǁFormFactorǁ__str____mutmut_orig.__name__ = 'xǁFormFactorǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class StorageType(models.Model):
    """
    Model to define storage types.
    """
    type = models.CharField(max_length=100, unique=True)  # Ensure the storage type name is unique

    def xǁStorageTypeǁ__str____mutmut_orig(self):
        return self.type  # String representation of the StorageType model

    xǁStorageTypeǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStorageTypeǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁStorageTypeǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁStorageTypeǁ__str____mutmut_orig)
    xǁStorageTypeǁ__str____mutmut_orig.__name__ = 'xǁStorageTypeǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['type'])  # Index the type field for faster search
        ]

# Motherboard models
class MotherboardQuerySet(models.QuerySet):
    def xǁMotherboardQuerySetǁby_ram_type__mutmut_orig(self, ram_type):
        return self.filter(ram__type=ram_type)
    def xǁMotherboardQuerySetǁby_ram_type__mutmut_1(self, ram_type):
        return self.filter(ram__type=None)

    xǁMotherboardQuerySetǁby_ram_type__mutmut_mutants = {
    'xǁMotherboardQuerySetǁby_ram_type__mutmut_1': xǁMotherboardQuerySetǁby_ram_type__mutmut_1
    }

    def by_ram_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMotherboardQuerySetǁby_ram_type__mutmut_orig"), object.__getattribute__(self, "xǁMotherboardQuerySetǁby_ram_type__mutmut_mutants"), *args, **kwargs)
        return result 

    by_ram_type.__signature__ = _mutmut_signature(xǁMotherboardQuerySetǁby_ram_type__mutmut_orig)
    xǁMotherboardQuerySetǁby_ram_type__mutmut_orig.__name__ = 'xǁMotherboardQuerySetǁby_ram_type'



class MotherboardManager(models.Manager):
    def xǁMotherboardManagerǁget_queryset__mutmut_orig(self):
        return MotherboardQuerySet(self.model, using=self._db)
    def xǁMotherboardManagerǁget_queryset__mutmut_1(self):
        return MotherboardQuerySet(self.model,)

    xǁMotherboardManagerǁget_queryset__mutmut_mutants = {
    'xǁMotherboardManagerǁget_queryset__mutmut_1': xǁMotherboardManagerǁget_queryset__mutmut_1
    }

    def get_queryset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMotherboardManagerǁget_queryset__mutmut_orig"), object.__getattribute__(self, "xǁMotherboardManagerǁget_queryset__mutmut_mutants"), *args, **kwargs)
        return result 

    get_queryset.__signature__ = _mutmut_signature(xǁMotherboardManagerǁget_queryset__mutmut_orig)
    xǁMotherboardManagerǁget_queryset__mutmut_orig.__name__ = 'xǁMotherboardManagerǁget_queryset'



    def xǁMotherboardManagerǁby_ram_type__mutmut_orig(self, ram_type):
        return self.get_queryset().by_ram_type(ram_type)

    def xǁMotherboardManagerǁby_ram_type__mutmut_1(self, ram_type):
        return self.get_queryset().by_ram_type(None)

    xǁMotherboardManagerǁby_ram_type__mutmut_mutants = {
    'xǁMotherboardManagerǁby_ram_type__mutmut_1': xǁMotherboardManagerǁby_ram_type__mutmut_1
    }

    def by_ram_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMotherboardManagerǁby_ram_type__mutmut_orig"), object.__getattribute__(self, "xǁMotherboardManagerǁby_ram_type__mutmut_mutants"), *args, **kwargs)
        return result 

    by_ram_type.__signature__ = _mutmut_signature(xǁMotherboardManagerǁby_ram_type__mutmut_orig)
    xǁMotherboardManagerǁby_ram_type__mutmut_orig.__name__ = 'xǁMotherboardManagerǁby_ram_type'



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

    def xǁMotherboardǁ__str____mutmut_orig(self):
        return self.name  # String representation of the Motherboard model

    xǁMotherboardǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMotherboardǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁMotherboardǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁMotherboardǁ__str____mutmut_orig)
    xǁMotherboardǁ__str____mutmut_orig.__name__ = 'xǁMotherboardǁ__str__'



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

    def xǁRAMTypeǁ__str____mutmut_orig(self):
        return self.type  # String representation of the RAMType model

    xǁRAMTypeǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMTypeǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRAMTypeǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRAMTypeǁ__str____mutmut_orig)
    xǁRAMTypeǁ__str____mutmut_orig.__name__ = 'xǁRAMTypeǁ__str__'



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

    def xǁRAMSpeedǁ__str____mutmut_orig(self):
        return f"{self.speed} MHz"  # String representation of the RAMSpeed model

    xǁRAMSpeedǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMSpeedǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRAMSpeedǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRAMSpeedǁ__str____mutmut_orig)
    xǁRAMSpeedǁ__str____mutmut_orig.__name__ = 'xǁRAMSpeedǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['speed'])  # Index the speed field for faster search
        ]

class RAMCapacity(models.Model):
    """
    Model to define RAM capacity (e.g., 16GB).
    """
    capacity = models.CharField(max_length=10)

    def xǁRAMCapacityǁ__str____mutmut_orig(self):
        return self.capacity  # String representation of the RAMCapacity model

    xǁRAMCapacityǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMCapacityǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRAMCapacityǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRAMCapacityǁ__str____mutmut_orig)
    xǁRAMCapacityǁ__str____mutmut_orig.__name__ = 'xǁRAMCapacityǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['capacity'])  # Index the capacity field for faster search
        ]

class RAMNumberOfModules(models.Model):
    """
    Model to define the number of RAM modules.
    """
    number_of_modules = models.IntegerField(validators=[MinValueValidator(1)])  # Ensure at least 1 module

    def xǁRAMNumberOfModulesǁ__str____mutmut_orig(self):
        return str(self.number_of_modules)  # String representation of the RAMNumberOfModules model

    xǁRAMNumberOfModulesǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMNumberOfModulesǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRAMNumberOfModulesǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRAMNumberOfModulesǁ__str____mutmut_orig)
    xǁRAMNumberOfModulesǁ__str____mutmut_orig.__name__ = 'xǁRAMNumberOfModulesǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['number_of_modules'])  # Index the number_of_modules field for faster search
        ]

class RAMManager(models.Manager):
    def xǁRAMManagerǁby_type__mutmut_orig(self, ram_type):
        return self.filter(ram_type__type=ram_type)
    def xǁRAMManagerǁby_type__mutmut_1(self, ram_type):
        return self.filter(ram_type__type=None)

    xǁRAMManagerǁby_type__mutmut_mutants = {
    'xǁRAMManagerǁby_type__mutmut_1': xǁRAMManagerǁby_type__mutmut_1
    }

    def by_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMManagerǁby_type__mutmut_orig"), object.__getattribute__(self, "xǁRAMManagerǁby_type__mutmut_mutants"), *args, **kwargs)
        return result 

    by_type.__signature__ = _mutmut_signature(xǁRAMManagerǁby_type__mutmut_orig)
    xǁRAMManagerǁby_type__mutmut_orig.__name__ = 'xǁRAMManagerǁby_type'



    def xǁRAMManagerǁby_speed_range__mutmut_orig(self, min_speed, max_speed):
        return self.filter(ram_speed__speed__gte=min_speed, ram_speed__speed__lte=max_speed)

    def xǁRAMManagerǁby_speed_range__mutmut_1(self, min_speed, max_speed):
        return self.filter(ram_speed__speed__gte=None, ram_speed__speed__lte=max_speed)

    def xǁRAMManagerǁby_speed_range__mutmut_2(self, min_speed, max_speed):
        return self.filter(ram_speed__speed__gte=min_speed, ram_speed__speed__lte=None)

    def xǁRAMManagerǁby_speed_range__mutmut_3(self, min_speed, max_speed):
        return self.filter( ram_speed__speed__lte=max_speed)

    def xǁRAMManagerǁby_speed_range__mutmut_4(self, min_speed, max_speed):
        return self.filter(ram_speed__speed__gte=min_speed,)

    xǁRAMManagerǁby_speed_range__mutmut_mutants = {
    'xǁRAMManagerǁby_speed_range__mutmut_1': xǁRAMManagerǁby_speed_range__mutmut_1, 
        'xǁRAMManagerǁby_speed_range__mutmut_2': xǁRAMManagerǁby_speed_range__mutmut_2, 
        'xǁRAMManagerǁby_speed_range__mutmut_3': xǁRAMManagerǁby_speed_range__mutmut_3, 
        'xǁRAMManagerǁby_speed_range__mutmut_4': xǁRAMManagerǁby_speed_range__mutmut_4
    }

    def by_speed_range(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMManagerǁby_speed_range__mutmut_orig"), object.__getattribute__(self, "xǁRAMManagerǁby_speed_range__mutmut_mutants"), *args, **kwargs)
        return result 

    by_speed_range.__signature__ = _mutmut_signature(xǁRAMManagerǁby_speed_range__mutmut_orig)
    xǁRAMManagerǁby_speed_range__mutmut_orig.__name__ = 'xǁRAMManagerǁby_speed_range'



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

    def xǁRAMǁclean__mutmut_orig(self):
        # Custom validation logic
        if self.ram_speed.speed not in range(800, 8001):
            raise ValidationError(f"RAM speed {self.ram_speed.speed} is out of the valid range.")

    def xǁRAMǁclean__mutmut_1(self):
        # Custom validation logic
        if self.ram_speed.speed  in range(800, 8001):
            raise ValidationError(f"RAM speed {self.ram_speed.speed} is out of the valid range.")

    def xǁRAMǁclean__mutmut_2(self):
        # Custom validation logic
        if self.ram_speed.speed not in range(801, 8001):
            raise ValidationError(f"RAM speed {self.ram_speed.speed} is out of the valid range.")

    def xǁRAMǁclean__mutmut_3(self):
        # Custom validation logic
        if self.ram_speed.speed not in range(800, 8002):
            raise ValidationError(f"RAM speed {self.ram_speed.speed} is out of the valid range.")

    xǁRAMǁclean__mutmut_mutants = {
    'xǁRAMǁclean__mutmut_1': xǁRAMǁclean__mutmut_1, 
        'xǁRAMǁclean__mutmut_2': xǁRAMǁclean__mutmut_2, 
        'xǁRAMǁclean__mutmut_3': xǁRAMǁclean__mutmut_3
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMǁclean__mutmut_orig"), object.__getattribute__(self, "xǁRAMǁclean__mutmut_mutants"), *args, **kwargs)
        return result 

    clean.__signature__ = _mutmut_signature(xǁRAMǁclean__mutmut_orig)
    xǁRAMǁclean__mutmut_orig.__name__ = 'xǁRAMǁclean'



    def xǁRAMǁ__str____mutmut_orig(self):
        return f"{self.name} {self.ram_type.type} {self.ram_speed.speed} MHz - {self.ram_number_of_modules.number_of_modules} x {self.ram_capacity.capacity}"  # Improved string representation

    xǁRAMǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRAMǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁRAMǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁRAMǁ__str____mutmut_orig)
    xǁRAMǁ__str____mutmut_orig.__name__ = 'xǁRAMǁ__str__'



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

    def xǁMicroarchitectureǁ__str____mutmut_orig(self):
        return self.name  # String representation of the Microarchitecture model

    xǁMicroarchitectureǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMicroarchitectureǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁMicroarchitectureǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁMicroarchitectureǁ__str____mutmut_orig)
    xǁMicroarchitectureǁ__str____mutmut_orig.__name__ = 'xǁMicroarchitectureǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['name'])  # Index the name field for faster search
        ]

class CPUMicroarchitectureManager(models.Manager):
    def xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_orig(self, name):
        return self.filter(microarchitecture__name=name)
    def xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_1(self, name):
        return self.filter(microarchitecture__name=None)

    xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_mutants = {
    'xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_1': xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_1
    }

    def by_microarchitecture(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_orig"), object.__getattribute__(self, "xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_mutants"), *args, **kwargs)
        return result 

    by_microarchitecture.__signature__ = _mutmut_signature(xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_orig)
    xǁCPUMicroarchitectureManagerǁby_microarchitecture__mutmut_orig.__name__ = 'xǁCPUMicroarchitectureManagerǁby_microarchitecture'



    def xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_orig(self, socket_type_name):
        return self.filter(socket_type__name=socket_type_name)

    def xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_1(self, socket_type_name):
        return self.filter(socket_type__name=None)

    xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_mutants = {
    'xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_1': xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_1
    }

    def by_socket_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_orig"), object.__getattribute__(self, "xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_mutants"), *args, **kwargs)
        return result 

    by_socket_type.__signature__ = _mutmut_signature(xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_orig)
    xǁCPUMicroarchitectureManagerǁby_socket_type__mutmut_orig.__name__ = 'xǁCPUMicroarchitectureManagerǁby_socket_type'



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

    objects = CPUMicroarchitectureManager()  # Use custom manager

    def xǁCPUǁ__str____mutmut_orig(self):
        return self.name  # String representation of the CPU model

    xǁCPUǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCPUǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCPUǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCPUǁ__str____mutmut_orig)
    xǁCPUǁ__str____mutmut_orig.__name__ = 'xǁCPUǁ__str__'



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

    def xǁStorageCapacityǁ__str____mutmut_orig(self):
        return self.capacity  # String representation of the StorageCapacity model

    xǁStorageCapacityǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStorageCapacityǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁStorageCapacityǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁStorageCapacityǁ__str____mutmut_orig)
    xǁStorageCapacityǁ__str____mutmut_orig.__name__ = 'xǁStorageCapacityǁ__str__'



    class Meta:
        indexes = [
            models.Index(fields=['capacity'])  # Index the capacity field for faster search
        ]

class StorageManager(models.Manager):
    def xǁStorageManagerǁby_type__mutmut_orig(self, storage_type):
        return self.filter(type__type=storage_type)
    def xǁStorageManagerǁby_type__mutmut_1(self, storage_type):
        return self.filter(type__type=None)

    xǁStorageManagerǁby_type__mutmut_mutants = {
    'xǁStorageManagerǁby_type__mutmut_1': xǁStorageManagerǁby_type__mutmut_1
    }

    def by_type(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStorageManagerǁby_type__mutmut_orig"), object.__getattribute__(self, "xǁStorageManagerǁby_type__mutmut_mutants"), *args, **kwargs)
        return result 

    by_type.__signature__ = _mutmut_signature(xǁStorageManagerǁby_type__mutmut_orig)
    xǁStorageManagerǁby_type__mutmut_orig.__name__ = 'xǁStorageManagerǁby_type'



    def xǁStorageManagerǁby_capacity_range__mutmut_orig(self, min_capacity, max_capacity):
        return self.filter(capacity__capacity__gte=min_capacity, capacity__capacity__lte=max_capacity)

    def xǁStorageManagerǁby_capacity_range__mutmut_1(self, min_capacity, max_capacity):
        return self.filter(capacity__capacity__gte=None, capacity__capacity__lte=max_capacity)

    def xǁStorageManagerǁby_capacity_range__mutmut_2(self, min_capacity, max_capacity):
        return self.filter(capacity__capacity__gte=min_capacity, capacity__capacity__lte=None)

    def xǁStorageManagerǁby_capacity_range__mutmut_3(self, min_capacity, max_capacity):
        return self.filter( capacity__capacity__lte=max_capacity)

    def xǁStorageManagerǁby_capacity_range__mutmut_4(self, min_capacity, max_capacity):
        return self.filter(capacity__capacity__gte=min_capacity,)

    xǁStorageManagerǁby_capacity_range__mutmut_mutants = {
    'xǁStorageManagerǁby_capacity_range__mutmut_1': xǁStorageManagerǁby_capacity_range__mutmut_1, 
        'xǁStorageManagerǁby_capacity_range__mutmut_2': xǁStorageManagerǁby_capacity_range__mutmut_2, 
        'xǁStorageManagerǁby_capacity_range__mutmut_3': xǁStorageManagerǁby_capacity_range__mutmut_3, 
        'xǁStorageManagerǁby_capacity_range__mutmut_4': xǁStorageManagerǁby_capacity_range__mutmut_4
    }

    def by_capacity_range(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStorageManagerǁby_capacity_range__mutmut_orig"), object.__getattribute__(self, "xǁStorageManagerǁby_capacity_range__mutmut_mutants"), *args, **kwargs)
        return result 

    by_capacity_range.__signature__ = _mutmut_signature(xǁStorageManagerǁby_capacity_range__mutmut_orig)
    xǁStorageManagerǁby_capacity_range__mutmut_orig.__name__ = 'xǁStorageManagerǁby_capacity_range'



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

    def xǁStorageǁ__str____mutmut_orig(self):
        return f"{self.name} - {self.form_factor.name} - {self.capacity.capacity}"  # String representation of the Storage model

    xǁStorageǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStorageǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁStorageǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁStorageǁ__str____mutmut_orig)
    xǁStorageǁ__str____mutmut_orig.__name__ = 'xǁStorageǁ__str__'



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

    def xǁSupportedRAMConfigurationǁ__str____mutmut_orig(self):
        return f"{self.motherboard.name} supports {self.ram}"  # String representation of the model

    xǁSupportedRAMConfigurationǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSupportedRAMConfigurationǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁSupportedRAMConfigurationǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁSupportedRAMConfigurationǁ__str____mutmut_orig)
    xǁSupportedRAMConfigurationǁ__str____mutmut_orig.__name__ = 'xǁSupportedRAMConfigurationǁ__str__'



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

    def xǁSupportedStorageConfigurationǁ__str____mutmut_orig(self):
        return f"{self.motherboard.name} supports {self.storage_type.type} with {self.slots} slots"  # String representation of the model

    xǁSupportedStorageConfigurationǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSupportedStorageConfigurationǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁSupportedStorageConfigurationǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁSupportedStorageConfigurationǁ__str____mutmut_orig)
    xǁSupportedStorageConfigurationǁ__str____mutmut_orig.__name__ = 'xǁSupportedStorageConfigurationǁ__str__'



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

    def xǁCPUMotherboardCompatibilityǁ__str____mutmut_orig(self):
        return f"{self.cpu.name} is compatible with {self.motherboard.name}"  # String representation of the model

    xǁCPUMotherboardCompatibilityǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCPUMotherboardCompatibilityǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCPUMotherboardCompatibilityǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCPUMotherboardCompatibilityǁ__str____mutmut_orig)
    xǁCPUMotherboardCompatibilityǁ__str____mutmut_orig.__name__ = 'xǁCPUMotherboardCompatibilityǁ__str__'



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

    def xǁBuildStorageConfigurationǁ__str____mutmut_orig(self):
        return f"{self.build.name} - {self.storage.name} ({self.role})"  # String representation of the model

    xǁBuildStorageConfigurationǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildStorageConfigurationǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁBuildStorageConfigurationǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁBuildStorageConfigurationǁ__str____mutmut_orig)
    xǁBuildStorageConfigurationǁ__str____mutmut_orig.__name__ = 'xǁBuildStorageConfigurationǁ__str__'



    class Meta:
        unique_together = ('build', 'storage')  # Ensure unique combinations of build and storage
        constraints = [
            models.CheckConstraint(condition=models.Q(role__in=['Primary', 'Secondary']), name='role_valid')
        ]
        indexes = [
            models.Index(fields=['build']),  # Index the build field for faster search
            models.Index(fields=['storage']),  # Index the storage field for faster search
        ]
