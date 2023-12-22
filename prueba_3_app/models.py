from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)

class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=200, blank=True)

class Seminario(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_in = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_in = models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=200, blank=True)
    inscritos = models.ManyToManyField(Inscrito)
