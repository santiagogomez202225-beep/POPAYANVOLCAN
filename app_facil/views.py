from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Temblor


def bienvenida_popayan(request):
    return render(request, 'app_facil/bienvenida_popayan.html')


def formulario_temblor(request):
    if request.method == 'POST':
        nuevo = Temblor()
        nuevo.nombre = request.POST.get('nombre')
        nuevo.magnitud = request.POST.get('magnitud')
        nuevo.profundidad = request.POST.get('profundidad')
        nuevo.rango = request.POST.get('rango')
        nuevo.lugar = request.POST.get('lugar')
        nuevo.area = request.POST.get('area')
        nuevo.fecha = request.POST.get('fecha') or None
        nuevo.hora = request.POST.get('hora') or None
        nuevo.save()
        return redirect('formulario_temblor')

    query = request.GET.get('q', '').strip()
    if query:
        temblores = Temblor.objects.filter(
            Q(nombre__icontains=query) |
            Q(lugar__icontains=query) |
            Q(area__icontains=query) |
            Q(rango__icontains=query) |
            Q(magnitud__icontains=query)
        ).order_by('-id')
    else:
        temblores = Temblor.objects.all().order_by('-id')

    return render(request, 'app_facil/temblor.html', {
        'temblores': temblores,
        'query': query,
    })


def listar_temblores(request):
    temblores = Temblor.objects.all().order_by('-id')
    return render(request, 'app_facil/listar_temblores.html', {'temblores': temblores})


def informe_temblor(request, id):
    temblor = get_object_or_404(Temblor, id=id)
    return render(request, 'app_facil/salida-temblor.html', {'temblor': temblor})