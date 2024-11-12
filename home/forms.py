from django import forms
from .models import Build
from .compatibility_service import CompatibilityService

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ['name', 'motherboard', 'cpu', 'ram', 'storage']

    def clean(self):
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
