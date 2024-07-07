from django.db import models
from django.utils import timezone

class Inventario(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre_producto
