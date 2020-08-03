from django.urls import path
from app.ddi import views as ddi
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ddi'

urlpatterns = [
    path('', ddi.index, name='index'),
    path('usuarios/', ddi.lista_usuarios, name='usuarios'),
    path('usuarios/editar/<str:pk>/', ddi.editar_usuario, name='editar_usuario'),
    path('expedientes/', ddi.lista_expedientes, name='expedientes'),
    path('expedientes/editar/<str:pk>/',
         ddi.editar_expediente, name='editar_expediente'),
    path('desarrolladoras/', ddi.lista_desarrolladoras, name='desarrolladoras'),
    path('desarrolladoras/editar/<str:pk>/',
         ddi.editar_desarrolladora, name='editar_desarrolladora'),
    path('categorias/', ddi.lista_categorias, name='categorias'),
    path('categorias/editar/<str:pk>/',
         ddi.editar_categoria, name='editar_categoria'),
    path('subcategorias/', ddi.lista_subcategorias, name='subcategorias'),
    path('subcategorias/editar/<str:pk>/',
         ddi.editar_subcategoria, name="editar_sub"),
    path('proyectos/', ddi.lista_proyectos, name="proyectos"),
    path('proyectos/detalles/<str:pk>/',
         ddi.lista_ingresos, name="ingresos"),
    path('proyectos/detalles/revisar/<str:pk>/',
         ddi.revisar_ingreso, name="revisar_ingreso"),
    path('proyectos/editar/<str:pk>/',
         ddi.editar_proyecto, name="ingresos"),
    path('proyectos/detalles/archivos/<str:pk>/', ddi.ver_archivos),
    path('user/proyectos/', ddi.usuario_proyectos),
    path('user/proyectos/ingresos/<str:pk>/', ddi.usuario_ingresos),
    path('user/proyectos/ingresos/archivos/<str:pk>/', ddi.ver_oficios),
    path('borrar/', ddi.eliminar, name='borrar'),
    path('reportes/', ddi.ver_reportes),
    path('reportes/nota_expediente/', ddi.reporte_nota_por_expediente),
    path('reportes/ingresos_diarios/', ddi.reporte_ingresos_por_dia),
    path('reportes/funcionarios/', ddi.reporte_funcionarios),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
