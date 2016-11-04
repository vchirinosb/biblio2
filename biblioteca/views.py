from django.shortcuts import render, get_object_or_404
from .forms import AutorForm, EditorialForm, LibroForm, LibroBuscarForm
from .models import Autor, Editorial, Libro
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect


# Create your views here.
def IndexView(request):
    template_name = 'biblioteca/index.html'
    return render(request, template_name, {})


###############
##   Autor   ##
###############
def AutorView(request):
    template_name = 'biblioteca/mtnautor/autor.html'
    form_class = AutorForm(request.POST or None)
    resultado = ""
    
    if form_class.is_valid():
        form_class.save()
        form_class = AutorForm()
        resultado = "AUTOR INGRESADO CON EXITO"
    
    #
    paginate_by = 10
    autores = Autor.objects.all()
    paginator = Paginator(autores, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        autores = paginator.page(page)
    except PageNotAnInteger:
        autores = paginator.page(1)
    except EmptyPage:
        autores = paginator.page(paginator.num_pages)
    #
    
    context = {
        "form": form_class, 
        "resultado": resultado, 
        "autores": autores
    }
    
    return render(request, template_name, context)


def AutorUpdate(request, id):
    template_name = 'biblioteca/mtnautor/autor.html'
    resultado = ""
    instance = get_object_or_404(Autor, id=id)
    form_class = AutorForm(request.POST or None, instance=instance)
    
    if form_class.is_valid():
        form_class.save()
        form_class = AutorForm()
        resultado = "AUTOR ACTUALIZADO CON EXITO"
        return HttpResponseRedirect('/biblioteca/autor')
    
    #
    paginate_by = 10
    autores = Autor.objects.all()
    paginator = Paginator(autores, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        autores = paginator.page(page)
    except PageNotAnInteger:
        autores = paginator.page(1)
    except EmptyPage:
        autores = paginator.page(paginator.num_pages)
    #
    
    context = {
        "form": form_class, 
        "resultado": resultado, 
        "autores": autores
    }
    
    return render(request, template_name, context)


def AutorDelete(request, id):
    
    # elimina en cascada, CORREGIR
    Autor.objects.get(pk=id).delete()
    resultado = "AUTOR ELIMINADO CON EXITO"
    
    return HttpResponseRedirect('/biblioteca/autor')


###############
## Editorial ##
###############
def EditorialView(request):
    template_name = 'biblioteca/mtneditorial/editorial.html'
    form_class = EditorialForm(request.POST or None)
    resultado = ""
    
    if form_class.is_valid():
        form_class.save()
        form_class = EditorialForm()
        resultado = "EDITORIAL INGRESADA CON EXITO"
    
    #
    paginate_by = 10
    editoriales = Editorial.objects.all()
    paginator = Paginator(editoriales, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        editoriales = paginator.page(page)
    except PageNotAnInteger:
        editoriales = paginator.page(1)
    except EmptyPage:
        editoriales = paginator.page(paginator.num_pages)
    #
    
    context = {
        "form": form_class, 
        "resultado": resultado, 
        "editoriales": editoriales
    }
    
    return render(request, template_name, context)


def EditorialUpdate(request, id):
    template_name = 'biblioteca/mtneditorial/editorial.html'
    resultado = ""
    instance = get_object_or_404(Editorial, id=id)
    form_class = EditorialForm(request.POST or None, instance=instance)
    
    if form_class.is_valid():
        form_class.save()
        form_class = EditorialForm()
        resultado = "EDITORIAL ACTUALIZADA CON EXITO"
        return HttpResponseRedirect('/biblioteca/editorial')
    
    #
    paginate_by = 10
    editoriales = Editorial.objects.all()
    paginator = Paginator(editoriales, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        editoriales = paginator.page(page)
    except PageNotAnInteger:
        editoriales = paginator.page(1)
    except EmptyPage:
        editoriales = paginator.page(paginator.num_pages)
    #
    
    context = {
        "form": form_class, 
        "resultado": resultado, 
        "editoriales": editoriales
    }
    
    return render(request, template_name, context)


def EditorialDelete(request, id):
    
    # elimina en cascada, CORREGIR
    Editorial.objects.get(pk=id).delete()
    resultado = "EDITORIAL ELIMINADA CON EXITO"
    
    return HttpResponseRedirect('/biblioteca/editorial')


###############
##   Libro   ##
###############
def LibroView(request):
    template_name = 'biblioteca/mtnlibro/libro.html'
    form_class = LibroForm(request.POST or None)
    resultado = ""
    
    if form_class.is_valid():
        form_class.save()
        form_class = LibroForm()
        resultado = "LIBRO INGRESADO CON EXITO"
    
    context = {
        "form": form_class, 
        "resultado": resultado
    }
    
    return render(request, template_name, context)


def LibroList(request):
    template_name = 'biblioteca/mtnlibro/lstlibro.html'
    form_class = LibroBuscarForm(request.POST or None)
    resultado = ""
    
    libros = Libro.objects.all()
    
    if form_class.is_valid():
        autor_tmp = form_class.cleaned_data['autor']
        titulo_tmp = form_class.cleaned_data['titulo']
        libros = Libro.objects.filter(autor__nombre__contains=autor_tmp, titulo__contains=titulo_tmp)
        resultado = "BUSQUEDA DE LIBROS REALIZADA"
    
    #
    paginate_by = 10
    paginator = Paginator(libros, paginate_by)
    
    page = request.GET.get('page')
    
    try:
        libros = paginator.page(page)
    except PageNotAnInteger:
        libros = paginator.page(1)
    except EmptyPage:
        libros = paginator.page(paginator.num_pages)
    #
    
    context = {
        "form": form_class, 
        "resultado": resultado, 
        "libros": libros
    }
    
    return render(request, template_name, context)

def LibroUpdate(request, id):
    template_name = 'biblioteca/mtnlibro/libro.html'
    resultado = ""
    instance = get_object_or_404(Libro, id=id)
    form_class = LibroForm(request.POST or None, instance=instance)
    
    if form_class.is_valid():
        form_class.save()
        form_class = LibroForm()
        resultado = "LIBRO ACTUALIZADO CON EXITO"
        return HttpResponseRedirect('/biblioteca/libro/listar')
    
    context = {
        "form": form_class, 
        "resultado": resultado
    }
    
    return render(request, template_name, context)

def LibroDelete(request, id):
    
    Libro.objects.get(pk=id).delete()
    resultado = "LIBRO ELIMINADO CON EXITO"
    
    return HttpResponseRedirect('/biblioteca/libro/listar')

