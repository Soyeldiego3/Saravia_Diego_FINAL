from rest_framework import serializers
from .models import Seminario, Institucion

class SeminarioSerial(serializers.ModelSerializer):
    Choices = (
        ("Reservado", "Reservado"),
        ("Completa", "Completa"),
        ("Anulada", "Anulada"),
        ("No Asisten", "No Asisten"),
    )

    estado = serializers.ChoiceField(choices=Choices, style={'class': 'form-control'})

    class Meta:
        model = Seminario
        fields = ['nombre', 'telefono', 'fecha_in', 'institucion', 'hora_in', 'estado', 'observacion']

class InstitucionSerial(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre']