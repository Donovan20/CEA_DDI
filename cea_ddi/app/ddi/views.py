from django.shortcuts import render
from django.shortcuts import redirect
from json import dumps
from django.http import HttpResponse

from app.ddi.models import Expediente
from app.ddi.forms import ExpForm
from app.ddi.models import Desarrolladora
from app.ddi.forms import DesaForm
from app.ddi.models import Categorias
from app.ddi.forms import CateForm
from app.ddi.models import SubCategorias
from app.ddi.forms import SubCateForm 

from re import compile

# Create your views here.

def index(request):

    return render(request,'dashboard.html')

def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    if request.method == 'POST':
        form = ExpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            folio = compile(r'^[A-z][A-z]\-[0-9][0-9][0-9]\-[0-9][0-9]\-[A-z]$')
            if folio.match(exp.numero):
                if Expediente.objects.filter(numero = exp.numero):
                    pass
                else:
                    exp.save()
                    return redirect('/expedientes/')
            else:
                pass
    else:
        form = ExpForm()
    return render(request,'expedientes.html',{'expedientes':expedientes,'form':form})    

def get_data(request):
    data = {}
    if request.POST['bandera'] == 'e':
        exp = Expediente.objects.get(pk = request.POST['pk'])
        data = {
            'numero' : exp.numero,
            'fraccionamiento' : exp.fraccionamiento,
            'pk':exp.pk
        }
        data = dumps(data)

    elif request.POST['bandera'] == 'd':
        desa = Desarrolladora.objects.get(pk = request.POST['pk'])
        data = {
            'representante' : desa.representante,
            'nombre' : desa.nombre,
            'propietario': desa.propietario,
            'pk':desa.pk
        }
        data = dumps(data)

    elif request.POST['bandera'] == 'c':
        cate = Categorias.objects.get(pk = request.POST['pk'])
        data = {
            'nombre' : cate.nombre,
            'pk': cate.pk
        }
        data = dumps(data)

    elif request.POST['bandera'] == 's':
        sub = SubCategorias.objects.get(pk = request.POST['pk'])
        data = SubCateForm(instance=sub)
        print(data.cleaned_data)
        data ={
            'categoria' : data['categoria'],
            'nombre': data['nombre'],
            'pk':sub.pk
        }
        data = dumps(data)

    return HttpResponse(data)



def editar_expediente(request):

    if request.method == 'POST':
        e = Expediente.objects.get(pk = request.POST['pk'])
        form = ExpForm(request.POST, instance=e)
        if form.is_valid():
            exp = form.save(commit=False)
            folio = compile(r'^[A-z][A-z]\-[0-9][0-9][0-9]\-[0-9][0-9]\-[A-z]$')
            if folio.match(exp.numero):
                if Expediente.objects.filter(numero = exp.numero):
                    pass
                else:
                    exp.save()
                    return redirect('/expedientes/')
    return HttpResponse('ok')

def eliminar(request):
    url = ""
    if request.POST['bandera'] == 'e':
        exp = Expediente.objects.get(pk = request.POST['pk'])
        exp.delete()
        url ='/expedientes/'

    elif request.POST['bandera'] == 'd':
        desa = Desarrolladora.objects.get(pk = request.POST['pk'])
        desa.delete()
        url = "/desarrolladoras/"
    
    elif request.POST['bandera'] == 'c':
        cate = Categorias.objects.get(pk = request.POST['pk'])
        cate.delete()
        url = "/categorias/"

    elif request.POST['bandera'] == 's':
        sub = SubCategorias.objects.get(pk = request.POST['pk'])
        sub.delete()
        url = "/subcategorias/"

    return HttpResponse(url)

def lista_desarrolladoras(request):
    desarrolladoras = Desarrolladora.objects.all()
    if request.method == 'POST':
        form = DesaForm(request.POST)
        if form.is_valid():
            des = form.save(commit=False)
            if Desarrolladora.objects.filter(nombre = des.nombre):
                pass
            else:
                des.save()
    else:
        form = DesaForm()
    return render(request,'desarrolladora.html',{'desarrolladoras':desarrolladoras,'form':form})

def editar_desarrolladora(request):
    if request.method == 'POST':
        d = Desarrolladora.objects.get(pk = request.POST['pk'])
        form = DesaForm(request.POST, instance=d)
        if form.is_valid():
            desa = form.save(commit=False)
            if Desarrolladora.objects.filter(nombre = desa.nombre):
                pass
            else:
                desa.save()
                return redirect('/desarrolladoras/')
    return HttpResponse('ok')

def lista_categorias(request):
    categorias = Categorias.objects.all()
    if request.method == 'POST':
        form = CateForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            if Categorias.objects.filter(nombre = cate.nombre):
                pass
            else:
                cate.save()
    else:
        form = CateForm()
    return render(request,'categorias.html',{'categorias':categorias,'form':form})


def editar_categoria(request):
    if request.method == 'POST':
        c = Categorias.objects.get(pk = request.POST['pk'])
        form = CateForm(request.POST, instance=c)
        if form.is_valid():
            cate = form.save(commit=False)
            if Categorias.objects.filter(nombre= cate.nombre):
                pass
            else:
                cate.save()
                return redirect('/categorias/')
    return HttpResponse('ok')

def lista_subcategorias(request):
    subcategorias = SubCategorias.objects.all()
    if request.method == 'POST':
        form = SubCateForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            if SubCategorias.objects.filter(nombre = sub.nombre):
                pass
            else:
                sub.save()
    else:
        form = SubCateForm()
    return render(request,'subcategorias.html',{'subcategorias':subcategorias,'form': form})


def editar_subcategoria(request,pk):
    subcategoria = SubCategorias.objects.get(pk = pk)
    if request.method == 'POST':
        form = SubCateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            pass
    else:
        form = SubCateForm(instance=subcategoria)
    return render(request,'',{'form':form})