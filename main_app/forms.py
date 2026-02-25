from django import forms
from .models import accessory

class Accessory(forms.ModelForm):
    class Meta:
        model = accessory
        fields = ['date']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }