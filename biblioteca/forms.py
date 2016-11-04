'''
Created on 2 nov. 2016

@author: Hugo
'''
from django import forms
from biblioteca.models import Autor, Editorial, Libro

class AutorForm(forms.ModelForm):
    
    descripcion = forms.CharField(max_length=450, required=False, widget=forms.Textarea(attrs={'cols': 100, 'rows': 5, 'class': 'form-control'}) )
    
    class Meta:
        model = Autor
        fields = ['nombre', 'descripcion']
        labels = {
            "nombre": "Nombre(*)",
            "descripcion": "Descripcion"
        }
    
    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class EditorialForm(forms.ModelForm):
    
    class Meta:
        model = Editorial
        fields = ['editorial']
        labels = {
            "editorial": "Editorial(*)"
        }
    
    def __init__(self, *args, **kwargs):
        super(EditorialForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = ['autor', 'editorial', 'titulo', 'anhopublicacion', 'edicion', 'imagenportada', 'cantidadejemplares']
        labels = {
            "autor": "Autor(*)",
            "editorial": "Editorial(*)",
            "titulo": "Titulo(*)",
            "anhopublicacion": "Anio de Publicacion(*)", 
            "edicion": "Edicion(*)", 
            "imagenportada": "Imagen de Portada", 
            "cantidadejemplares": "Cantidad de Ejemplares(*)"   
        }
    
    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class LibroBuscarForm(forms.Form):
    
    autor = forms.CharField(label='Autor', max_length=200, required=False)
    titulo = forms.CharField(label='Titulo', max_length=250, required=False)
    
    class Meta:
        fields = ['autor', 'titulo']
    
    def __init__(self, *args, **kwargs):
        super(LibroBuscarForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
