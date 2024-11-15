
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


from django import forms
from .models import Build
from .compatibility_service import CompatibilityService

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ['name', 'motherboard', 'cpu', 'ram', 'storage']

    def xǁBuildFormǁclean__mutmut_orig(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_1(self):
        cleaned_data = None
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_2(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('XXmotherboardXX')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_3(self):
        cleaned_data = super().clean()
        motherboard = None
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_4(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('XXcpuXX')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_5(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = None
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_6(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('XXramXX')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_7(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = None
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_8(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('XXstorageXX')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_9(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = None

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_10(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=None, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_11(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=None, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_12(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=None)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_13(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build( cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_14(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_15(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu,)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_16(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = None
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_17(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(None)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_18(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(None)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data

    def xǁBuildFormǁclean__mutmut_19(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storage = cleaned_data.get('storage')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storage=storage)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(None))

        return cleaned_data

    xǁBuildFormǁclean__mutmut_mutants = {
    'xǁBuildFormǁclean__mutmut_1': xǁBuildFormǁclean__mutmut_1, 
        'xǁBuildFormǁclean__mutmut_2': xǁBuildFormǁclean__mutmut_2, 
        'xǁBuildFormǁclean__mutmut_3': xǁBuildFormǁclean__mutmut_3, 
        'xǁBuildFormǁclean__mutmut_4': xǁBuildFormǁclean__mutmut_4, 
        'xǁBuildFormǁclean__mutmut_5': xǁBuildFormǁclean__mutmut_5, 
        'xǁBuildFormǁclean__mutmut_6': xǁBuildFormǁclean__mutmut_6, 
        'xǁBuildFormǁclean__mutmut_7': xǁBuildFormǁclean__mutmut_7, 
        'xǁBuildFormǁclean__mutmut_8': xǁBuildFormǁclean__mutmut_8, 
        'xǁBuildFormǁclean__mutmut_9': xǁBuildFormǁclean__mutmut_9, 
        'xǁBuildFormǁclean__mutmut_10': xǁBuildFormǁclean__mutmut_10, 
        'xǁBuildFormǁclean__mutmut_11': xǁBuildFormǁclean__mutmut_11, 
        'xǁBuildFormǁclean__mutmut_12': xǁBuildFormǁclean__mutmut_12, 
        'xǁBuildFormǁclean__mutmut_13': xǁBuildFormǁclean__mutmut_13, 
        'xǁBuildFormǁclean__mutmut_14': xǁBuildFormǁclean__mutmut_14, 
        'xǁBuildFormǁclean__mutmut_15': xǁBuildFormǁclean__mutmut_15, 
        'xǁBuildFormǁclean__mutmut_16': xǁBuildFormǁclean__mutmut_16, 
        'xǁBuildFormǁclean__mutmut_17': xǁBuildFormǁclean__mutmut_17, 
        'xǁBuildFormǁclean__mutmut_18': xǁBuildFormǁclean__mutmut_18, 
        'xǁBuildFormǁclean__mutmut_19': xǁBuildFormǁclean__mutmut_19
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBuildFormǁclean__mutmut_orig"), object.__getattribute__(self, "xǁBuildFormǁclean__mutmut_mutants"), *args, **kwargs)
        return result 

    clean.__signature__ = _mutmut_signature(xǁBuildFormǁclean__mutmut_orig)
    xǁBuildFormǁclean__mutmut_orig.__name__ = 'xǁBuildFormǁclean'


