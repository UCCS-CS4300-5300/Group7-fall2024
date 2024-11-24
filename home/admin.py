# admin.py
from django.contrib import admin
from .models import Profile, ShoppingCart, Build, Manufacturer
from .models import CPU, CPUSocketType, Microarchitecture, Motherboard 
from .models import FormFactor, StorageCapacity, StorageType, Storage
from .models import RAM, RAMCapacity, RAMNumberOfModules, RAMSpeed, RAMType, BuildRAM
from .compatibility_service import CompatibilityService


class RAMInline(admin.TabularInline):
    model = BuildRAM
    extra = 4


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'cpu_socket_type')
    search_fields = ('name',)
    list_filter = ('manufacturer', 'cpu_socket_type')


class CPUAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'name', 'socket_type')
    search_fields = ('name',)
    list_filter = ('manufacturer', 'socket_type')


@admin.action(description='Check Build Compatibility')
def check_build_compatibility(modeladmin, request, queryset):
    for build in queryset:
        try:
            CompatibilityService.check_build_compatibility(build)
            modeladmin.message_user(request, f'Build "{build.name}" is compatible.')
        except ValueError as e:
            modeladmin.message_user(request, f'Build "{build.name}" compatibility error: {str(e)}', level='error')


class BuildAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'is_complete', 'motherboard', 'cpu')
    list_filter = ('is_complete',)
    inlines = [RAMInline]
    actions = [check_build_compatibility]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)


admin.site.register(Profile)
admin.site.register(ShoppingCart)
admin.site.register(Manufacturer)
admin.site.register(CPUSocketType)
admin.site.register(Microarchitecture)
admin.site.register(FormFactor)  # Updated here
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
