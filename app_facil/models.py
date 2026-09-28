from django.db import models


class Temblor(models.Model):
    nombre = models.CharField(max_length=100)
    magnitud = models.FloatField()
    profundidad = models.FloatField(null=True, blank=True)
    rango = models.CharField(max_length=100, null=True, blank=True)
    lugar = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Temblor {self.nombre} - Magnitud {self.magnitud}"