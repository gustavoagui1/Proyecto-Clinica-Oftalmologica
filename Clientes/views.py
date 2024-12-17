from django.shortcuts import render, redirect, get_object_or_404
from Clientes.models import Paciente

#------------------------------>HAY QUE AJUSTAR ESTO A CLIENTES<---------------------------------------------------------

def index(request): #READ
    return render(request, 'index.html')

def lista_reservas(request):#VER SI AGREGAR ESTO O NO
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/lista_pacientes.html', {'pacientes': pacientes})

def agregar_reserva(request): #CREATE
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        cantidad_personas = request.POST['cantidad_personas']
        estado = request.POST['estado']
        observacion = request.POST.get('observacion', '')
        Reserva.objects.create(
            nombre=nombre, telefono=telefono, fecha=fecha,
            hora=hora, cantidad_personas=cantidad_personas,
            estado=estado, observacion=observacion
        )
        return redirect('lista_reservas')
    return render(request, 'reservas/agregar_reserva.html')

def editar_reserva(request, id): #UPDATE
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.nombre = request.POST['nombre']
        reserva.telefono = request.POST['telefono']
        reserva.fecha = request.POST['fecha']
        reserva.hora = request.POST['hora']
        reserva.cantidad_personas = request.POST['cantidad_personas']
        reserva.estado = request.POST['estado']
        reserva.observacion = request.POST.get('observacion', '')
        reserva.save()
        return redirect('lista_reservas')
    return render(request, 'reservas/editar_reserva.html', {'reserva': reserva})

def eliminar_reserva(request, id): #DELETE
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')
    return render(request, 'reservas/eliminar_reserva.html', {'reserva': reserva})