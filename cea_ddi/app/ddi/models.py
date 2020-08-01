from django.db import models
from django.contrib.auth.models import User
from cea_ddi.settings import MEDIA_URL

# Create your models here.


class Expediente(models.Model):
    numero = models.CharField(max_length=11)
    fraccionamiento = models.CharField(max_length=150)

    def __str__(self):
        return str(self.numero)


class Desarrolladora(models.Model):
    representante = models.CharField(max_length=150)
    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.nombre + " - " + self.representante)


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)


class SubCategorias(models.Model):

    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre + " - " + self.categoria.__str__())


class Estados(models.Model):

    s = (
        ('A', 'Aprobado'),
        ('E', 'En espera de reingreso'),
        ('R', 'En revision'),
        ('I', 'Revisado')
    )
    status = models.CharField(max_length=1, default='R')
    nombre = models.CharField(max_length=50, default='En revision')

    def __str__(self):
        return str(self.nombre)


class Proyectos(models.Model):
    nombre = models.CharField(max_length=150)
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    desarrolladora = models.ForeignKey(
        Desarrolladora, on_delete=models.CASCADE)
    tipo = models.ForeignKey(SubCategorias, on_delete=models.CASCADE)
    responsable = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='responsable')
    revisador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='revisador')
    ingreso = models.IntegerField()


class Ingresos(models.Model):
    ingreso = models.IntegerField()
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    status = models.ForeignKey(Estados, on_delete=models.CASCADE)
    folio = models.CharField(max_length=13)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False)
    fecha_programada = models.DateField(auto_now=False, auto_now_add=False)
    oficio = models.CharField(max_length=14, null=True, blank=True)
    fecha_respuesta = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    dias = models.IntegerField(null=True, blank=True)


class Files(models.Model):
    file = models.FileField(
        null=True, blank=True, upload_to='')
    ingreso = models.ForeignKey(Ingresos, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)


class Aprobados(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    gasto_m3_seg = models.IntegerField()
    vivienda = models.CharField(max_length=50)
    costo = models.IntegerField()
