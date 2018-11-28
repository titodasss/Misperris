
from django.urls import path
from .views import home, formulario,listarMascota,eliminarMascota,listarAdoptador,eliminarAdoptador,modificarAdoptador,agregarMascota



urlpatterns = [
    path('', home, name="home"),
    path('formulario/',formulario,name="formulario"),
    path('listarAdoptador/',listarAdoptador,name="listadoAdoptador"),
    path('eliminarAdoptador/<run>/',eliminarAdoptador,name="eliminarAdoptador"),
    path('modificarAdoptador/<run>/',modificarAdoptador,name="modificarAdoptador"),
    path('agregarMascota/',agregarMascota,name="agregarMascota"),
    path('listarMascota/', listarMascota, name="listarMascota"),
    path('eliminarMascota/<id>/', eliminarMascota, name="eliminarMascota"),
]
