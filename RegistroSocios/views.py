
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.models import Persona

def index(request):
    return render(request, 'core/index.html', {})