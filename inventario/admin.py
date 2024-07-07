from django.contrib import admin
from .models import Inventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'cantidad', 'precio', 'fecha_ingreso')
    search_fields = ('nombre_producto',)
    list_filter = ('cantidad', 'precio')
    ordering = ('nombre_producto',)
