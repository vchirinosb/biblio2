from django.contrib import admin
from .models import Autor, Editorial, Libro

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ["__str__", "descripcion"]
    class Meta:
        model = Autor

class EditorialAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Editorial

class LibroAdmin(admin.ModelAdmin):
    class Meta:
        model = Libro

admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Libro, LibroAdmin)
