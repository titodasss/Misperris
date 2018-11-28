from django.contrib import admin
from .models import Region,Ciudad,TipoVivienda,Postulante,Mascota
# Register your models here.

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('run','nombre','apellido','fechaNacimiento','email','telefono','region','ciudad','tipoVivienda')
    search_fields=['run','apellido']
    
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre','genero','fecha_ingreso','fecha_nacimiento','imagen_mascota','estado','raza')
    search_fields=['id','nombre']
    list_filter = ('raza',)


admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(TipoVivienda)
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Mascota, MascotaAdmin)
