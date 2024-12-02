from django import forms
from Oftalmologos.models import Oftalmologo

class OftalmologoForm(forms.ModelForm):
    class Meta:
        model = Oftalmologo
        fields = ['nombre_doctor', 'apellido_doctor', 'rut_doctor']
        widgets = {
            'nombre_doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del doctor'}),
            'apellido_doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido del doctor'}),
            'rut_doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT del doctor'}),
        }