
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from RegistroSocios.models import Persona
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
#mixin - tarea


def index(request):
    return render(request, 'RegistroSocios/index.html', {})

def facial(request):
    return render(request, 'RegistroSocios/facial.html', {})

def qr(request):
    return render(request, 'RegistroSocios/qr.html', {})


class PersonaCreate(CreateView,):
    model = Persona
    fields = ['nombre','apellido','genero','direccion','telefono','condicion_civil', 'puesto_idpuesto', 'categoria_idcategoria']
    success_url = reverse_lazy('crear_registro')


