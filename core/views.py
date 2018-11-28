from django.shortcuts import render, redirect
from .models import Ciudad,Region,TipoVivienda,Postulante,Mascota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
# Create your views here.

def home(resquest):
    return render(resquest, 'core/home.html')

#CRUD postulantes
def formulario(request):
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    tipoviviendas = TipoVivienda.objects.all()

    variables = {
        'regiones':regiones,
        'ciudades':ciudades,
        'tipoviviendas':tipoviviendas
    }
    
    if request.POST:
        postul = Postulante()
        postul.run = request.POST.get('txtRun')
        postul.nombre = request.POST.get('txtNombre')
        postul.apellido = request.POST.get('txtApellido')
        postul.fechaNacimiento = request.POST.get('Fecha')
        postul.email = request.POST.get('txtEmail')
        postul.telefono = request.POST.get('txtTelefono')
        #region
        region = Region()
        region.id = request.POST.get('cboRegion')
        postul.region = region
        #ciudad
        ciudad = Ciudad()                
        ciudad.id = request.POST.get('cboCiudad')        
        postul.ciudad = ciudad
        #tipo vivienda        
        tipovivienda = TipoVivienda()
        tipovivienda.id = request.POST.get('cboTipoVivienda')
        postul.tipoVivienda = tipovivienda

        try:
            postul.save()            
            variables['mensaje'] = 'Guardado correctamente'            
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/formulario.html', variables)

def listarAdoptador(request):

    adoptador = Postulante.objects.all()

    return render(request,'core/listar_adoptador.html',{
        'adoptadores':adoptador
    })

def eliminarAdoptador(request, run):
    adoptador = Postulante.objects.get(run=run)

    try:
        adoptador.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request,mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)
    return redirect('listado_adoptador')

def modificarAdoptador(request,run):
    adoptador = Postulante.objects.get(run=run)
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    tipoviviendas = TipoVivienda.objects.all()

    variables = {
        'adoptador':adoptador,
        'regiones':regiones,
        'ciudades':ciudades,
        'tipoviviendas':tipoviviendas
    }

    if request.POST:
        postul = Postulante()
        
        postul.run = request.POST.get('txtId')
        postul.nombre = request.POST.get('txtNombre')
        postul.apellido = request.POST.get('txtApellido')
        postul.fechaNacimiento = request.POST.get('Fecha')
        postul.email = request.POST.get('txtEmail')
        postul.telefono = request.POST.get('txtTelefono')
        #region
        region = Region()
        region.id = request.POST.get('cboRegion')
        postul.region = region
        #ciudad
        ciudad = Ciudad()                
        ciudad.id = request.POST.get('cboCiudad')        
        postul.ciudad = ciudad
        #tipo vivienda        
        tipovivienda = TipoVivienda()
        tipovivienda.id = request.POST.get('cboTipoVivienda')
        postul.tipoVivienda = tipovivienda

        try:
            postul.save()            
            messages.success(request, 'modificado correctamente')            
        except:
            messages.error(request, 'no se ha podido modificar')   
        return redirect('listado_adoptador') 

    return render(request,'core/modificar_adoptador.html',variables)

#CRUD mascotas
@login_required
def agregarMascota(request): 
    grabo=False

    if request.POST:
        form = DocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            
            #masco = Mascota()
            #masco.fecha_ingreso = request.POST.get('FechaI')
            #masco.fecha_nacimiento = request.POST.get('FechaN')

            masco = form.save(commit=False)
            masco.fecha_ingreso = request.POST.get('FechaI')
            masco.fecha_nacimiento = request.POST.get('FechaN')
            masco.save()
            
            grabo=True  
            form = DocumentForm()
    else:
        form = DocumentForm()  

    return render(request, 'core/agregar_mascota.html', {'form':form,'grabo':grabo})

def listarMascota(request):
    
    mascota = Mascota.objects.all()
    return render(request,'core/listar.html',{
        'mascotas':mascota})

def eliminarMascota(request,id):
    mascota = Mascota.objects.get(id=id)
    
    try:
        
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)

    return redirect('listarMascota')
    




    
    