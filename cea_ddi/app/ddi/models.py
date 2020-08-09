from django.db import models
from django.contrib.auth.models import AbstractUser
from cea_ddi.settings import MEDIA_URL

# Create your models here.


class Usuario(AbstractUser):
    imagen = models.FileField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
        Usuario, on_delete=models.CASCADE, related_name='responsable')
    revisor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='revisor')
    status = models.ForeignKey(Estados, on_delete=models.CASCADE)
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
    observaciones = models.TextField(null=True, blank=True)


class Files(models.Model):
    file = models.FileField(
        null=True, blank=True, upload_to='')
    ingreso = models.ForeignKey(Ingresos, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)
