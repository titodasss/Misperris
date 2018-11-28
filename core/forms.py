from django import forms
from .models import Mascota

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = (
            'nombre', 
            'raza',
            'estado',
            'genero',
            #'fecha_ingreso',
            #'fecha_nacimiento',            
            'imagen_mascota',
            )
        labels={
            'nombre':'Nombre',
            'raza':'Raza',
            'estado':'Estado',
            'genero':'Genero',
            #'fecha_ingreso':'Fecha Ingreso',
            #'fecha_nacimiento':'Fecha Nacimiento',
            'imagen_mascota':'Imagen Mascota',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'raza':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control'}),
            #'fecha_ingreso':forms.DateField,
            #'fecha_nacimiento':forms.DateField,
            'imagen_mascota':forms.FileInput(attrs={'required':True}),
        }

