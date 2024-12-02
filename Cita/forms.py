from django import forms
from Cita.models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['hora_cita','fecha_cita','oftalmologo']#Hya que entregar los datos del paciente mediante las vistas
        widgets = {
            'hora_cita': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'fecha_cita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'oftalmologo': forms.Select(attrs={'class': 'form-control'}),
        }