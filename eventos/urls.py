from django.urls import path
from . import views

# ¡Importante! El 'app_name' es necesario para la función {% url 'eventos:inscripcion' ... %}
app_name = 'eventos'

urlpatterns = [
    # Esta es una ruta de ejemplo para la página de inscripción del evento
    path('<slug:slug>/inscripcion/', views.inscripcion_view, name='inscripcion'),
    # Deberías crear esta vista 'inscripcion_view' en views.py
]