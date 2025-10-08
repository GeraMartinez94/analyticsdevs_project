import requests
import os 
from django.shortcuts import render

# ====================================================================
# CONFIGURACIÓN SIN GITHUB TOKEN
# ====================================================================
GITHUB_USERNAME = "GeraMartinez94"

# 🛑 ¡IMPORTANTE! ELIMINAMOS GITHUB_TOKEN.
# Ya no es necesario y esta parte del código queda 100% segura.

# --------------------------------------------------------------------
# DATOS DE PROYECTOS FIJADOS (HARDCODED) - SEGURO Y EFICIENTE
# --------------------------------------------------------------------
# Debes llenar esta lista con la información de tus repositorios.
FEATURED_REPOS = [
    {
        'name': "Reconocimiento_gestos_Python",
        'description': "Proyecto de visión por computadora para reconocer gestos con la mano.",
        'html_url': "https://github.com/GeraMartinez94/Reconocimiento_gestos_Python",
        'language': "Python",
        'updated_at': "2024-05-15T10:00:00Z" # Fecha solo para formato visual
    },
    {
        'name': "Scrapting_Python",
        'description': "Scripts y herramientas para la extracción de datos de la web.",
        'html_url': "https://github.com/GeraMartinez94/Scrapting_Python",
        'language': "Python",
        'updated_at': "2024-04-01T10:00:00Z"
    },
    {
        'name': "Data-Analytics-Python",
        'description': "Análisis de datos, visualización y modelos predictivos en Python.",
        'html_url': "https://github.com/GeraMartinez94/Data-Analytics-Python",
        'language': "Python",
        'updated_at': "2024-03-20T10:00:00Z"
    },
    {
        'name': "Project_graphic_python",
        'description': "Proyectos con interfaz gráfica usando Tkinter o PyQt.",
        'html_url': "https://github.com/GeraMartinez94/Project_graphic_python",
        'language': "Python",
        'updated_at': "2024-02-10T10:00:00Z"
    }
    # Puedes añadir más si tu diseño lo permite
]
# ====================================================================


def get_language_color(language):
    """Devuelve un color de lenguaje común de GitHub."""
    colors = {
        "Python": "#3572A5", "JavaScript": "#f1e05a", "HTML": "#e34c26",
        "CSS": "#563d7c", "TypeScript": "#2b7489", "Jupyter Notebook": "#DA5B0B",
        "C#": "#178600", "PHP": "#4F5D95", "Java": "#b07219",
        "Go": "#00ADD8", "Shell": "#89e051", "SQL": "#e38200", 
    }
    return colors.get(language, "#CCCCCC") 


def get_github_data():
    """
    Obtiene lenguajes de forma estática y retorna los repositorios fijados desde la lista local.
    Hemos eliminado las llamadas a la API que requieren el GITHUB_TOKEN.
    """
    
    # ------------------------------------------------
    # 🛑 Lógica de Lenguajes Simplificada (o estática)
    # Si quieres eliminar el token por completo, esta sección también debe ser estática.
    # Usaremos una lista estática para simplificar y eliminar la dependencia de la API.
    # ------------------------------------------------
    
    language_percentages = [
        {'language': 'Python', 'percent': 75.00, 'color': get_language_color('Python')},
        {'language': 'JavaScript', 'percent': 15.00, 'color': get_language_color('JavaScript')},
        {'language': 'HTML', 'percent': 6.00, 'color': get_language_color('HTML')},
        {'language': 'CSS', 'percent': 4.00, 'color': get_language_color('CSS')},
    ]

    return {
        'languages': language_percentages, # Usamos la lista estática
        'featured_repos': FEATURED_REPOS,  # Usamos la lista local y segura
    }


def home_view(request):
    """Vista principal que renderiza la página y pasa los datos de GitHub."""
    
    data = get_github_data()
    languages = data['languages']
    
    # Prepara los datos para el conic-gradient de CSS (Gráfico de Torta)
    current_stop = 0
    gradient_parts = []
    for lang in languages:
        next_stop = current_stop + lang['percent']
        gradient_parts.append(f"{lang['color']} {current_stop:.2f}% {next_stop:.2f}%")
        current_stop = next_stop

    gradient_string = ", ".join(gradient_parts)
    
    context = {
        'languages': languages,
        'gradient_string': gradient_string,
        'featured_repos': data['featured_repos'], # <-- Estos son los datos locales ahora
    }
    
    return render(request, 'home.html', context)