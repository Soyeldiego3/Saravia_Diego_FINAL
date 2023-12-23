from django.shortcuts import render, redirect
from .serializers import SeminarioSerial, InstitucionSerial
from .models import Seminario, Institucion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

# Create your views here.
def RenderIndex(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def RenderSeminario(request):
    if request.method == 'GET':
        semi = Seminario.objects.all()
        return render(request, 'listado.html', {'seminarios': semi})
    
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
    
@api_view(['GET'])
def Usuario(request):
    datos_autor = {
        'username': "Diego Saravia",
        'Seccion': "IEI-171-N4",
    }
    return Response(datos_autor)


class ListadoSeminario(APIView):
    def get(self, request):
        inscritos =Seminario.objects.all()
        serial = SeminarioSerial(inscritos,many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = SeminarioSerial(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
class ListadoInstituciones(APIView):
    def get(self, request):
        inscritos =Institucion.objects.all()
        serial = InstitucionSerial(inscritos,many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InstitucionSerial(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status = status.HTTP_201_CREATED)
        return Response(serial.errors,status = status.HTTP_400_BAD_REQUEST)
    
def buscar_id(request):
    if request.method == 'POST':
        id_buscar = request.POST.get('id_buscar')
        return redirect(f'/detalle/{id_buscar}/')

    return render(request, 'buscar_id.html')

class DetalleView(RetrieveAPIView):
    queryset = Seminario.objects.all()
    serializer_class = SeminarioSerial