from django.db import models

# Create your models here.

class Region(models.Model):
    #id_region = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Ciudad(models.Model):
    #id_ciudad = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class TipoVivienda(models.Model):
    #id_vivienda = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion 

    class Meta:
        verbose_name = "Tipo Vivienda"
        verbose_name_plural = "Tipos de Vivienda"
#pendiente
class Postulante(models.Model):
    run = models.CharField(max_length=50,unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField(auto_now=True)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.run

    class Meta:
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"
###############################################################
###############################################################
# MASCOTA
class Mascota(models.Model):
    nombre = models.CharField(max_length =50,verbose_name='Nombre Mascota')
    raza = models.CharField(max_length=50,verbose_name='Raza')
    estado = (('Disponible','Disponible'),('Rescatado','Rescatado'),('Adoptado','Adoptado'))
    estado = models.CharField(max_length=50,choices=estado,default='Rescatado',verbose_name='Estado')
    genero = (('M','M'),('H','H'))
    genero = models.CharField(max_length=50,choices=genero,default='M',verbose_name='Genero')
    fecha_ingreso = models.DateField()
    fecha_nacimiento = models.DateField()
    imagen_mascota = models.ImageField(upload_to='fotos',blank=True,null=True)
        
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"