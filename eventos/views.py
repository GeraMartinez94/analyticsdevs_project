from django.shortcuts import render, get_object_or_404, redirect
from .models import Conferencia, Inscripcion
# from .forms import InscripcionForm # Necesitarías crear un formulario para esto

def inscripcion_view(request, slug):
    conferencia = get_object_or_404(Conferencia, slug=slug)
    
    # Aquí iría la lógica de POST para guardar el formulario de Inscripcion
    
    context = {'conferencia': conferencia}
    # Asegúrate de crear este archivo de plantilla
    return render(request, 'eventos/inscripcion.html', context)