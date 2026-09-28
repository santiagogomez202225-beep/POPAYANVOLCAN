from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida_popayan, name='inicio'),
    path('bienvenida/', views.bienvenida_popayan, name='bienvenida_popayan'),
    path('temblor/', views.formulario_temblor, name='formulario_temblor'),
    path('listar/', views.listar_temblores, name='listar_temblores'),
    path('informe/<int:id>/', views.informe_temblor, name='informe_temblor'),
]