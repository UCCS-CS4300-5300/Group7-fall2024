from django import forms
from .models import Build
from .compatibility_service import CompatibilityService

class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ['name', 'motherboard', 'cpu', 'ram', 'storages']  

    def clean(self):
        # Just perform regular validation; compatibility checks can be done in the view after saving
        return super().clean()
