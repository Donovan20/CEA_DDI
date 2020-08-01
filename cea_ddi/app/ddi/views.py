from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.db.models import Q
from wsgiref.util import FileWrapper

from django.contrib.auth.models import User
from cea_ddi.settings import BASE_DIR
from app.ddi.forms import UserForm
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
from app.ddi.models import Ingresos
from app.ddi.forms import IngresoForm
from app.ddi.forms import RevisarForm
from app.ddi.models import Files
from app.ddi.models import Estados

import os
from datetime import timedelta
from datetime import datetime
from re import compile
from json import dumps


def index(request):
    p = Proyectos.objects.filter(responsable=request.user).count()
    p2 = Proyectos.objects.filter(revisador=request.user).count
    return render(request, 'dashboard.html', {'proyectos': p, 'exp': p2})


def lista_usuarios(request):
    usuarios = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            if User.objects.filter(username=u.email):
                pass
            else:
                s = slice(3)
                p = u.first_name[s] + u.last_name[s] + ".@"
                u.password = make_password(p)
                u.username = u.email
                u.save()
                return redirect('/usuarios/')
    else:
        form = UserForm()
    return render(request, 'users.html', {'usuarios': usuarios, 'form': form})


def editar_usuario(request, pk):
    u = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=u)
        if form.is_valid():
            us = form.save(commit=False)
            if User.objects.filter(username=us.email):
                pass
            else:
                us.save()
                return redirect('/usuarios/')
    else:
        form = UserForm(instance=u)

    return render(request, 'editUser.html', {'form': form})


def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    if request.method == 'POST':
        form = ExpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            folio = compile(
                r'^[A-z][A-z]\-[0-9][0-9][0-9]\-[0-9][0-9]\-[A-z]$')
            if folio.match(exp.numero):
                if Expediente.objects.filter(numero=exp.numero):
                    pass
                else:
                    exp.save()
                    return redirect('/expedientes/')
            else:
                pass
    else:
        form = ExpForm()
    return render(request, 'expedientes.html', {'expedientes': expedientes, 'form': form})


def editar_expediente(request, pk):

    e = Expediente.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpForm(request.POST, instance=e)
        if form.is_valid():
            exp = form.save(commit=False)
            folio = compile(
                r'^[A-z][A-z]\-[0-9][0-9][0-9]\-[0-9][0-9]\-[A-z]$')
            if folio.match(exp.numero):
                if Expediente.objects.filter(numero=exp.numero):
                    pass
                else:
                    exp.save()
                    return redirect('/expedientes/')
    else:
        form = ExpForm(instance=e)
        print(form)
    return render(request, 'editExpediente.html', {'form': form})


def eliminar(request):
    url = ""
    if request.POST['bandera'] == 'e':
        exp = Expediente.objects.get(pk=request.POST['pk'])
        exp.delete()
        url = '/expedientes/'

    elif request.POST['bandera'] == 'd':
        desa = Desarrolladora.objects.get(pk=request.POST['pk'])
        desa.delete()
        url = "/desarrolladoras/"

    elif request.POST['bandera'] == 'c':
        cate = Categorias.objects.get(pk=request.POST['pk'])
        cate.delete()
        url = "/categorias/"

    elif request.POST['bandera'] == 's':
        sub = SubCategorias.objects.get(pk=request.POST['pk'])
        sub.delete()
        url = "/subcategorias/"

    return HttpResponse(url)


def lista_desarrolladoras(request):
    desarrolladoras = Desarrolladora.objects.all()
    if request.method == 'POST':
        form = DesaForm(request.POST)
        if form.is_valid():
            des = form.save(commit=False)
            if Desarrolladora.objects.filter(nombre=des.nombre):
                pass
            else:
                des.save()
    else:
        form = DesaForm()
    return render(request, 'desarrolladora.html', {'desarrolladoras': desarrolladoras, 'form': form})


def editar_desarrolladora(request, pk):
    d = Desarrolladora.objects.get(pk=pk)
    if request.method == 'POST':
        form = DesaForm(request.POST, instance=d)
        if form.is_valid():
            desa = form.save(commit=False)
            if Desarrolladora.objects.filter(nombre=desa.nombre):
                pass
            else:
                desa.save()
                return redirect('/desarrolladoras/')
    else:
        form = DesaForm(instance=d)
        print(form)
    return render(request, 'editDesarrolladora.html', {'form': form})


def lista_categorias(request):
    categorias = Categorias.objects.all()
    if request.method == 'POST':
        form = CateForm(request.POST)
        if form.is_valid():
            cate = form.save(commit=False)
            if Categorias.objects.filter(nombre=cate.nombre):
                pass
            else:
                cate.save()
    else:
        form = CateForm()
    return render(request, 'categorias.html', {'categorias': categorias, 'form': form})


def editar_categoria(request, pk):
    c = Categorias.objects.get(pk=pk)
    if request.method == 'POST':
        form = CateForm(request.POST, instance=c)
        if form.is_valid():
            cate = form.save(commit=False)
            if Categorias.objects.filter(nombre=cate.nombre):
                pass
            else:
                cate.save()
                return redirect('/categorias/')
    else:
        form = CateForm(instance=c)

    return render(request, 'editCategoria.html', {'form': form})


def lista_subcategorias(request):
    subcategorias = SubCategorias.objects.all()
    if request.method == 'POST':
        form = SubCateForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            if SubCategorias.objects.filter(nombre=sub.nombre):
                pass
            else:
                sub.save()
                return redirect('/subcategorias/')
    else:
        form = SubCateForm()
    return render(request, 'subcategorias.html', {'subcategorias': subcategorias, 'form': form})


def editar_subcategoria(request, pk):
    subcategoria = SubCategorias.objects.get(pk=pk)
    if request.method == 'POST':
        form = SubCateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            sub = form.save(commit=False)
            if SubCategorias.objects.filter(nombre=sub.nombre):
                pass
            else:
                sub.save()
                return redirect('/subcategorias/')
    else:
        form = SubCateForm(instance=subcategoria)

    return render(request, 'editSubcategoria.html', {'form': form})


def lista_proyectos(request):
    proyectos = Proyectos.objects.filter(revisador=request.user)
    print(proyectos)
    if request.method == 'POST':
        form = ProyeForm(request.POST)
        if form.is_valid():
            proy = form.save(commit=False)
            if Proyectos.objects.filter(expediente=proy.expediente):
                pass
            else:
                proy.ingreso = 0
                proy.save()
                return redirect('/proyectos/')
    else:
        form = ProyeForm()
    return render(request, 'proyectos.html', {'proyectos': proyectos, 'form': form})


def lista_ingresos(request, pk):
    ingresos = Ingresos.objects.filter(proyecto__pk=pk)
    return render(request, "ingresos.html", {'ingresos': ingresos})


def revisar_ingreso(request, pk):
    ingreso = Ingresos.objects.get(pk=pk)
    if request.method == 'POST':
        form = RevisarForm(request.POST, request.FILES, instance=ingreso)
        print(request.FILES)
        if form.is_valid():
            i = form.save(commit=False)
            s = Estados.objects.get(status='E')
            p = Proyectos.objects.get(pk=i.proyecto.pk)
            path = "planos\\"+p.expediente.numero+"\\"+i.folio+"\\"
            i.status = s
            i.save()
            for file in request.FILES.getlist('files'):
                f = Files(file=file, ingreso=ingreso, tipo="Respuesta")
                f.file.storage.location = path
                f.save()
            return redirect('/proyectos/detalles/'+str(p.pk)+"/")
        print(form.errors)
    else:
        form = RevisarForm(instance=ingreso)

    return render(request, 'revisar_ingreso.html', {'form': form})


def editar_proyecto(request, pk):
    p = Proyectos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProyeEditForm(request.POST, instance=p)
        if form.is_valid():
            print("paso")
            proye = form.save(commit=False)
            proye.save()
            return redirect('/proyectos/detalles/'+proye.expediente.numero+'/')
        else:
            print(form.errors)
    else:
        form = ProyeEditForm(instance=p)

    return render(request, 'editProye.html', {'form': form})


def usuario_proyectos(request):
    proyectos = Proyectos.objects.filter(responsable=request.user)
    return render(request, 'mis_proyectos.html', {'proyectos': proyectos})


def usuario_ingresos(request, pk):
    ingresos = Ingresos.objects.filter(proyecto__pk=pk)
    if request.method == 'POST':
        form = IngresoForm(request.POST, request.FILES)
        if form.is_valid():
            i = form.save(commit=False)
            if Ingresos.objects.filter(folio=i.folio):
                pass
            else:
                s = Estados.objects.get(status='R')
                p = Proyectos.objects.get(pk=pk)
                path = "planos\\"+p.expediente.numero+"\\"
                if os.path.exists(os.path.join(BASE_DIR, path)):
                    path = path + i.folio+"\\"
                    if os.path.exists(os.path.join(BASE_DIR, path)):
                        pass
                    else:
                        os.mkdir(os.path.join(BASE_DIR, path))
                else:
                    os.mkdir(os.path.join(BASE_DIR, path))
                    path = path + i.folio+"\\"
                    if os.path.exists(os.path.join(BASE_DIR, path)):
                        pass
                    else:
                        os.mkdir(os.path.join(BASE_DIR, path))
                i.status = s
                i.proyecto = p
                d = timedelta(days=21)
                i.fecha_programada = i.fecha_ingreso + d
                i.ingreso = p.ingreso + 1
                i.save()
                for file in request.FILES.getlist('files'):
                    f = Files(file=file, ingreso=i, tipo="Ingreso")
                    f.file.storage.location = os.path.join(BASE_DIR, path)
                    f.save()
                p.ingreso += 1
                p.save()
                return redirect('/user/proyectos/ingresos/'+pk+"/")
    else:
        form = IngresoForm()

    return render(request, "mis_ingresos.html", {'ingresos': ingresos, 'form': form})


def ver_archivos(request, pk):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    ingreso = Ingresos.objects.get(pk=pk)
    fs = Files.objects.filter(ingreso__pk=pk).filter(tipo="Ingreso")
    files = []
    for f in fs:
        aux = {}
        path = "http://127.0.0.1:8000/planos/"+ingreso.proyecto.expediente.numero + \
            "/"+ingreso.folio+"/"+str(f.file)
        aux['path'] = path
        aux['name'] = str(f.file)
        files.append(aux)
    print(files)
    return render(request, "archivos.html", {'files': files})


def ver_oficios(request, pk):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    ingreso = Ingresos.objects.get(pk=pk)
    fs = Files.objects.filter(ingreso__pk=pk).filter(tipo="Respuesta")
    files = []
    for f in fs:
        aux = {}
        path = "http://127.0.0.1:8000/planos/"+ingreso.proyecto.expediente.numero + \
            "/"+ingreso.folio+"/"+str(f.file)
        aux['path'] = path
        aux['name'] = str(f.file)
        files.append(aux)
    print(files)
    return render(request, "archivos.html", {'files': files})
