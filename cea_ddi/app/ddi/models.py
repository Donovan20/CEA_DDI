from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expediente(models.Model):
    numero = models.CharField(max_length=11)
    fraccionamiento = models.CharField(max_length=150)

class Desarrolladora(models.Model):
    representante = models.CharField(max_length=150)
    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=150, blank=True, null = True)

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)

class SubCategorias(models.Model):

    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

class Estados(models.Model):
    
    s = (
        ('A','Aprobado'),
        ('E', 'En espera de reingreso'),
        ('R', 'En revision')
    )  
    status = models.CharField(max_length=1,choices=s, default='R')

class Proyectos(models.Model):
    nombre = models.CharField(max_length=150)
    expediente = models.ForeignKey(Expediente,on_delete=models.CASCADE)
    desarrolladora = models.ForeignKey(Desarrolladora, on_delete= models.CASCADE)
    tipo = models.ForeignKey(SubCategorias, on_delete=models.CASCADE)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsable')
    revisador = models.ForeignKey(User,on_delete=models.CASCADE, related_name='revisador')
    status = models.ForeignKey(Estados,on_delete= models.CASCADE)
    folio = models.CharField(max_length=13)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False)
    fecha_programada = models.DateField(auto_now=False, auto_now_add=False)
    oficio = models.CharField(max_length=14)
    fecha_respuesta = models.DateField(auto_now=False, auto_now_add=False)
    ingreso = models.IntegerField()
    observaciones = models.CharField(max_length=300)
    archivo = models.FileField(null= True,blank= True)

class Aprobados(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete = models.CASCADE)
    gasto_m3_seg = models.IntegerField()
    vivienda = models.CharField(max_length=50)
    costo = models.IntegerField()