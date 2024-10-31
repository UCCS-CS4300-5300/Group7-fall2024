from django.contrib import admin
from .models import Profile, Shopping_Cart, Build, Manufacturer
from .models import CPU, CPUSocketType, Microarchitecture, Motherboard 
from .models import StorageFormFactor, StorageCapacity, StorageType,  Storage
from .models import RAM, RAMCapacity, RAMNumberOfModules, RAMSpeed, RAMType, BuildRAM

class RAMInline(admin.TabularInline):
    model = BuildRAM
    extra = 4


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'motherboard_manufacturer', 'cpu_socket_type')
    search_fields = ('name',)
    list_filter = ('motherboard_manufacturer', 'cpu_socket_type')

class CPUAdmin(admin.ModelAdmin):
    list_display = ('cpu_manufacturer', 'cpu_name', 'socket_type')
    search_fields = ('cpu_name',)
    list_filter = ('cpu_manufacturer', 'socket_type')

class BuildAdmin(admin.ModelAdmin):
    list_display = ('profile', 'is_complete', 'motherboard', 'cpu', 'storage')
    search_fields = ('profile__user__username',)
    list_filter = ('is_complete',)
    inlines = [RAMInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)
    
admin.site.register(Profile)
admin.site.register(Shopping_Cart)

admin.site.register(Manufacturer)
admin.site.register(CPUSocketType)
admin.site.register(Microarchitecture)
admin.site.register(StorageFormFactor)
admin.site.register(StorageCapacity)
admin.site.register(StorageType)
admin.site.register(Storage)
admin.site.register(RAM)
admin.site.register(RAMCapacity)
admin.site.register(RAMNumberOfModules)
admin.site.register(RAMSpeed)
admin.site.register(RAMType)

admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(CPU, CPUAdmin)
admin.site.register(Build, BuildAdmin)