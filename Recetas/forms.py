from django import forms
from Recetas.models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['receta', 'paciente']
        widgets = {
            'receta': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba su receta aquí'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
        }