from django import forms
from Clientes.models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre_paciente','apellido_paciente','rut_paciente']
        widgets = {
            'nombre_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del paciente'}),
            'apellido_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido del paciente'}),
            'rut_paciente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT del paciente'}),
        }