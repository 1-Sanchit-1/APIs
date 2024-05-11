from django import forms
from .models import CropData

class CropDataForm(forms.ModelForm):
    class Meta:
        model = CropData
        fields = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall','result']
