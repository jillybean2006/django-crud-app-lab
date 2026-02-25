from django import forms
from .models import Accessory

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }