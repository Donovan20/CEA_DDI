from django.shortcuts import render

from app.ddi.models import Expediente
from app.ddi.forms import ExpForm
from app.ddi.models import Desarrolladora
from app.ddi.forms import DesaForm
from app.ddi.models import Categorias
from app.ddi.forms import CateForm
from app.ddi.models import SubCategorias
from app.ddi.forms import SubCateForm 

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

def lista_categorias(request):
    categorias = Categorias.objects.all()
    return render(request,'',{'categorias':categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CateForm()
    return render(request,'',{'form':form})

def editar_categoria(request,pk):
    categoria = Categorias.objects.get(pk = pk)
    if request.method == 'POST':
        form = CateForm(request.POST, instance=categoria)
        if form.is_valid():
            pass
    else:
        form = CateForm(instance=categoria)
    return render(request,'',{'form':form})

def lista_subcategorias(request):
    subcategorias = SubCategorias.objects.all()
    return render(request,'',{'subcategorias':subcategorias})

def agregar_subcategoria(request):
    if request.method == 'POST':
        form = SubCateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SubCateForm()
    return render(request,'',{'form':form})

def editar_subcategoria(request,pk):
    subcategoria = SubCategorias.objects.get(pk = pk)
    if request.method == 'POST':
        form = SubCateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            pass
    else:
        form = SubCateForm(instance=subcategoria)
    return render(request,'',{'form':form})