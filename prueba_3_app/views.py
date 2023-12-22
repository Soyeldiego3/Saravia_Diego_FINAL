from django.shortcuts import render, redirect
from .serializers import SeminarioSerial, InstitucionSerial
from .models import Seminario, Institucion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def RenderSeminario(request):
    if request.method == 'GET':
        semi = Seminario.objects.all()
        return render(request, 'index.html', {'seminarios': semi})
    
@api_view(['GET', 'POST'])
def Agregar(request):
    if request.method == 'GET':
        seminarios = Seminario.objects.all()
        instituciones = Institucion.objects.all()
        return render(request, 'agregar.html', {'seminarios': seminarios, 'instituciones': instituciones})

    if request.method == 'POST':
        serializer = SeminarioSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('Agregar')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def instituciones(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerial(instituciones, many=True)
        return render(request, 'instituciones.html', {'instituciones': serializer.data})

    elif request.method == 'POST':
        serializer = InstitucionSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('instituciones')
        return render(request, 'instituciones.html', {'form': serializer})