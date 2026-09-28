from django.contrib import admin
from .models import Temblor


@admin.register(Temblor)
class TemblorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'magnitud', 'profundidad', 'lugar', 'area', 'fecha', 'hora')
    list_filter = ('lugar', 'area', 'fecha')
    search_fields = ('nombre', 'lugar', 'area', 'rango')
    ordering = ('-id',)