from django import forms
from Recetas.models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['receta', 'paciente', 'oftalmologo']
        widgets = {
            'receta': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalle de la receta'}),
            'paciente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del paciente'}),
            'oftalmologo': forms.Select(attrs={'class': 'form-control'}),
        }