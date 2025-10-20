from django.http import JsonResponse
import requests
import os 
from django.shortcuts import render
from openai import OpenAI 
from django.conf import settings
from django.views.decorators.http import require_http_methods

GITHUB_USERNAME = "GeraMartinez94"


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
    },
      {
        'name': "analyticsdevs_project", # El nombre del repositorio
        'description': "El portafolio dinámico con Django, PythonAnywhere y GitHub.",
        'html_url': "https://github.com/GeraMartinez94/analyticsdevs_project",
        'language': "Python",
        'updated_at': "2025-10-07T10:00:00Z" # Usa la fecha actual
    }
]

def contacto_view(request):
    # Por ahora, solo renderiza la plantilla contacto.html
    # Más adelante, aquí irá la lógica de tu formulario de contacto
    return render(request, 'core/contacto.html', {}) 


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

# --- LÓGICA DEL CHATBOT ---

@require_http_methods(["POST"])
def chat_api(request):
    """Maneja la comunicación con la API de OpenAI."""
    
    # Se usa request.POST porque el HTML usa content-type application/x-form-urlencoded
    user_message = request.POST.get('message', '') 
    
    if not user_message:
        return JsonResponse({'error': 'No se proporcionó un mensaje.'}, status=400)

    try:
        # Inicializa el cliente usando la clave cargada de settings.py
        client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente IA amigable y experto en Analítica y Desarrollo de Software."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
        )

        bot_reply = response.choices[0].message.content
        
        return JsonResponse({'reply': bot_reply})

    except Exception as e:
        print(f"Error al conectar con OpenAI: {e}")
        return JsonResponse({'error': 'Lo siento, el asistente IA está experimentando problemas técnicos.'}, status=500)


# --- VISTA PRINCIPAL (Corregida: se eliminó el duplicado) ---

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
        'messages': request.GET.getlist('messages'), 
        'languages': languages,
        'gradient_string': gradient_string,
        'featured_repos': data['featured_repos'],
        # ¡IMPORTANTE! Necesitamos el token CSRF para el fetch en el HTML
        'csrf_token': request.META.get('CSRF_COOKIE', ''), 
    }
    
    return render(request, 'home.html', context)