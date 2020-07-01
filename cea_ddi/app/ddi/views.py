from django.shortcuts import render

from app.ddi.models import Expediente
from app.ddi.forms import ExpForm
from app.ddi.models import Desarrolladora
from app.ddi.forms import DesaForm

import re

# Create your views here.

def index(request):

    return render(request,'index.html')

def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    return render(request,'',{'expedientes':expedientes})    

def agregar_expediente(request):
    if request.method == 'POST':
        form = ExpForm(request.POST)
        if form.is_valid():
            folio = ''
            pass
    else:
        form = ExpForm()
    return render(request,'',{'form':form})

def editar_expediente(request,pk):
    expediente = Expediente.objects.get(pk = pk)
    if request.method == 'POST':
        form = ExpForm(request.POST, instance=expediente)
        if form.is_valid():
            folio = ''
            pass
    else:
        form = ExpForm(instance=expediente)
    return render(request,'',{'form':form})

def lista_desarrolladoras(request):
    desarrolladoras = Desarrolladora.objects.all()
    return render(request,'',{'desarrolladoras':desarrolladoras})

def agregar_desarrolladora(request):
    if request.method == 'POST':
        form = DesaForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = DesaForm()
    return render(request,'',{'form':form})

def editar_desarrolladora(request,pk):
    desarrolladora = Desarrolladora.objects.get(pk = pk)
    if request.method == 'POST':
        form = DesaForm(request.POST, instance=desarrolladora)
        if form.is_valid():
            pass
    else:
        form = DesaForm(instance=desarrolladora)
    return render(request,'',{'form':form})