from django.contrib import admin
from .models import Seccion, Producto

# Register your models here.

class SeccionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Producto, ProductoAdmin)