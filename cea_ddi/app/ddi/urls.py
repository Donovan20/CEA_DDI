from django.urls import path
from app.ddi import views as ddi

app_name = 'ddi'

urlpatterns = [
    path('',ddi.index,name='index'),
    path('expedientes/',ddi.lista_expedientes,name='expedientes'),
    path('expedientes/editar/',ddi.editar_expediente,name='editar_expediente'),
    path('desarrolladoras/', ddi.lista_desarrolladoras, name='desarrolladoras'),
    path('desarrolladoras/editar/', ddi.editar_desarrolladora, name='editar_desarrolladora'),
    path('categorias/', ddi.lista_categorias, name='categorias'),
    path('categorias/editar/', ddi.editar_categoria, name='categorias'), 
    path('subcategorias/', ddi.lista_subcategorias, name='subcategorias'),
    path('obtener/',ddi.get_data,name='det_data'),
    path('borrar/',ddi.eliminar, name='borrar'),

]