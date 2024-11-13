from django import forms
from .models import Build
from .compatibility_service import CompatibilityService

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ['name', 'motherboard', 'cpu', 'ram', 'storages']

    def clean(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        cpu = cleaned_data.get('cpu')
        ram = cleaned_data.get('ram')
        storages = cleaned_data.get('storages')

        # Create a temporary build instance to check compatibility
        build = Build(motherboard=motherboard, cpu=cpu, storages=storages)
        build.ram.set(ram)

        try:
            CompatibilityService.check_build_compatibility(build)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        return cleaned_data
