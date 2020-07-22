from django.urls import path
from app.ddi import views as ddi

app_name = 'ddi'

urlpatterns = [
    path('',ddi.index,name='index'),
    path('expedientes/',ddi.lista_expedientes,name='expedientes'),
    path('expedientes/editar/<str:pk>/',ddi.editar_expediente,name='editar_expediente'),
    path('desarrolladoras/', ddi.lista_desarrolladoras, name='desarrolladoras'),
    path('desarrolladoras/editar/<str:pk>/', ddi.editar_desarrolladora, name='editar_desarrolladora'),
    path('categorias/', ddi.lista_categorias, name='categorias'),
    path('categorias/editar/<str:pk>/', ddi.editar_categoria, name='editar_categoria'), 
    path('subcategorias/', ddi.lista_subcategorias, name='subcategorias'),
    path('subcategorias/editar/<str:pk>/', ddi.editar_subcategoria, name ="editar_sub"),
    path('proyectos/',ddi.lista_proyectos, name ="proyectos"),
    path('proyectos/detalles/<str:expediente>/',ddi.lista_ingresos, name ="ingresos"),
    path('proyectos/detalles/editar/<str:pk>/',ddi.editar_proyecto, name ="ingresos"),
    path('borrar/',ddi.eliminar, name='borrar'),

]