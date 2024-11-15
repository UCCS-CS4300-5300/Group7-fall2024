
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

    def xǁBuildAdminǁsave_related__mutmut_orig(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_1(self, request, form, formsets, change):
        super().save_related(None, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_2(self, request, form, formsets, change):
        super().save_related(request, None, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_3(self, request, form, formsets, change):
        super().save_related(request, form, None, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_4(self, request, form, formsets, change):
        super().save_related(request, form, formsets, None)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_5(self, request, form, formsets, change):
        super().save_related( form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_6(self, request, form, formsets, change):
        super().save_related(request, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_7(self, request, form, formsets, change):
        super().save_related(request, form, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_8(self, request, form, formsets, change):
        super().save_related(request, form, formsets,)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_9(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(None, 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_10(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'XXvalidate_max_memoryXX'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_11(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr( 'validate_max_memory'):
                formset.validate_max_memory(formset)

    def xǁBuildAdminǁsave_related__mutmut_12(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            if hasattr(formset, 'validate_max_memory'):
                formset.validate_max_memory(None)

    xǁBuildAdminǁsave_related__mutmut_mutants = {
    'xǁBuildAdminǁsave_related__mutmut_1': xǁBuildAdminǁsave_related__mutmut_1, 
        'xǁBuildAdminǁsave_related__mutmut_2': xǁBuildAdminǁsave_related__mutmut_2, 
        'xǁBuildAdminǁsave_related__mutmut_3': xǁBuildAdminǁsave_related__mutmut_3, 
        'xǁBuildAdminǁsave_related__mutmut_4': xǁBuildAdminǁsave_related__mutmut_4, 
        'xǁBuildAdminǁsave_related__mutmut_5': xǁBuildAdminǁsave_related__mutmut_5, 
        'xǁBuildAdminǁsave_related__mutmut_6': xǁBuildAdminǁsave_related__mutmut_6, 
        'xǁBuildAdminǁsave_related__mutmut_7': xǁBuildAdminǁsave_related__mutmut_7, 
        'xǁBuildAdminǁsave_related__mutmut_8': xǁBuildAdminǁsave_related__mutmut_8, 
        'xǁBuildAdminǁsave_related__mutmut_9': xǁBuildAdminǁsave_related__mutmut_9, 
        'xǁBuildAdminǁsave_related__mutmut_10': xǁBuildAdminǁsave_related__mutmut_10, 
        'xǁBuildAdminǁsave_related__mutmut_11': xǁBuildAdminǁsave_related__mutmut_11, 
        'xǁBuildAdminǁsave_related__mutmut_12': xǁBuildAdminǁsave_related__mutmut_12
    }

    def save_related(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildAdminǁsave_related__mutmut_orig"), object.__getattribute__(self, "xǁBuildAdminǁsave_related__mutmut_mutants"), *args, **kwargs)
        return result 

    save_related.__signature__ = _mutmut_signature(xǁBuildAdminǁsave_related__mutmut_orig)
    xǁBuildAdminǁsave_related__mutmut_orig.__name__ = 'xǁBuildAdminǁsave_related'




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
