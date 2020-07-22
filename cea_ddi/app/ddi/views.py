from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.http import HttpResponse

from app.ddi.models import Expediente
from app.ddi.forms import ExpForm
from app.ddi.models import Desarrolladora
from app.ddi.forms import DesaForm
from app.ddi.models import Categorias
from app.ddi.forms import CateForm
from app.ddi.models import SubCategorias
from app.ddi.forms import SubCateForm 
from app.ddi.models import Proyectos
from app.ddi.forms import ProyeForm
from app.ddi.forms import ProyeEditForm
from app.ddi.models import Estados

from datetime import timedelta
from re import compile
from json import dumps



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

def editar_expediente(request, pk):

    e = Expediente.objects.get(pk = pk)
    if request.method == 'POST':
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
    else:
        form = ExpForm(instance=e)
        print(form)
    return render(request,'editExpediente.html',{'form':form})

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

def editar_desarrolladora(request, pk):
    d = Desarrolladora.objects.get(pk = pk)
    if request.method == 'POST':
        form = DesaForm(request.POST, instance=d)
        if form.is_valid():
            desa = form.save(commit=False)
            if Desarrolladora.objects.filter(nombre = desa.nombre):
                pass
            else:
                desa.save()
                return redirect('/desarrolladoras/')
    else:
        form = DesaForm(instance=d)
        print(form)
    return render(request,'editDesarrolladora.html',{'form':form})

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

def editar_categoria(request, pk):
    c = Categorias.objects.get(pk = pk)
    if request.method == 'POST':
        form = CateForm(request.POST, instance=c)
        if form.is_valid():
            cate = form.save(commit=False)
            if Categorias.objects.filter(nombre= cate.nombre):
                pass
            else:
                cate.save()
                return redirect('/categorias/')
    else:
        form = CateForm(instance=c)
        
    return render(request,'editCategoria.html',{'form':form})

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
                return redirect('/subcategorias/')
    else:
        form = SubCateForm()
    return render(request,'subcategorias.html',{'subcategorias':subcategorias,'form': form})

def editar_subcategoria(request,pk):
    subcategoria = SubCategorias.objects.get(pk = pk)
    if request.method == 'POST':
        form = SubCateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            sub = form.save(commit=False)
            if SubCategorias.objects.filter(nombre = sub.nombre):
                pass
            else:
                sub.save()
                return redirect('/subcategorias/')
    else:
        form = SubCateForm(instance=subcategoria)

    return render(request,'editSubcategoria.html',{'form':form})

def lista_proyectos(request):
    proyectos = Proyectos.objects.values("expediente__numero","desarrolladora__nombre","nombre","responsable__username", "revisador__username").annotate(num_ingresos = Count("expediente"))
    if request.method == 'POST':
        form = ProyeForm(request.POST)
        if form.is_valid():
            proy = form.save(commit=False)
            if Proyectos.objects.filter(expediente=proy.expediente):
                pass
            else:    
                s = Estados.objects.get(status='R')
                proy.status = s
                d = timedelta(days=21)
                print(type(proy.fecha_ingreso))
                proy.fecha_programada = proy.fecha_ingreso + d
                proy.ingreso = 1
                proy.save()
                return redirect('/proyectos/')
    else:
        form = ProyeForm()
    return render(request,'proyectos.html',{'proyectos':proyectos,'form': form})

def lista_ingresos(request, expediente):
    proyectos = Proyectos.objects.filter(expediente__numero = expediente)
    return render(request, "ingresos.html", {'proyectos': proyectos})

def editar_proyecto(request,pk):
    p = Proyectos.objects.get(pk = pk)
    if request.method == 'POST':
        form = ProyeEditForm(request.POST, instance=p)
        if form.is_valid():
            proye = form.save(commit=False)
            proye.save()
            return redirect('/proyectos/ingresos/'+proye.expediente.numero+'/')
    else:
        form = ProyeEditForm(instance=p)
        
    return render(request,'editProye.html',{'form':form})   
