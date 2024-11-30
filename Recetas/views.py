from django.shortcuts import render
from Recetas.models import Receta
# Create your views here.

def recetasData(request):
    recetas = Receta.objects.all()
    data = {'recetas':recetas}
    return render(request, 'Recetas/recetas.html',data)