from django.http import JsonResponse
import requests
import os 
from django.shortcuts import render
from google import genai
from google.genai import types
from django.conf import settings
from django.views.decorators.http import require_http_methods
import markdown # <--- 1. IMPORTAR LA LIBRERÍA MARKDOWN

GITHUB_USERNAME = "GeraMartinez94"

FEATURED_REPOS = [
    {
        'name': "Reconocimiento_gestos_Python",
        'description': "Proyecto de visión por computadora para reconocer gestos con la mano.",
        'html_url': "https://github.com/GeraMartinez94/Reconocimiento_gestos_Python",
        'language': "Python",
        'updated_at': "2024-05-15T10:00:00Z" 
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
        'name': "analyticsdevs_project", 
        'description': "El portafolio dinámico con Django, PythonAnywhere y GitHub.",
        'html_url': "https://github.com/GeraMartinez94/analyticsdevs_project",
        'language': "Python",
        'updated_at': "2025-10-07T10:00:00Z" 
    }
]

def contacto_view(request):
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
    """Obtiene lenguajes de forma estática y repositorios fijados desde la lista local."""
    
    language_percentages = [
        {'language': 'Python', 'percent': 75.00, 'color': get_language_color('Python')},
        {'language': 'JavaScript', 'percent': 15.00, 'color': get_language_color('JavaScript')},
        {'language': 'HTML', 'percent': 6.00, 'color': get_language_color('HTML')},
        {'language': 'CSS', 'percent': 4.00, 'color': get_language_color('CSS')},
    ]

    return {
        'languages': language_percentages, 
        'featured_repos': FEATURED_REPOS,  
    }


# ------------------------------------------------------------------
# --- LÓGICA DEL CHATBOT CON CONVERSIÓN MARKDOWN A HTML ---
# ------------------------------------------------------------------

@require_http_methods(["POST"])
def chat_api(request):
    """Maneja la comunicación con la API de Google Gemini y convierte la respuesta a HTML."""
    
    user_message = request.POST.get('message', '') 
    
    if not user_message:
        return JsonResponse({'error': 'No se proporcionó un mensaje.'}, status=400)

    if not settings.GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY no está configurada en settings.py.")
        return JsonResponse({'error': 'Error de configuración: La clave de Gemini no se encontró.'}, status=500)

    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        
        system_instruction = (
            "Eres un asistente IA amigable y experto en Analítica de Datos, Python, Django y desarrollo web. "
            "Tu objetivo es responder preguntas sobre mi portafolio y habilidades de forma profesional y concisa. "
            "**SIEMPRE utiliza formato Markdown (como **negritas**, *cursivas*, y listas con *) para resaltar conceptos clave y mejorar la lectura.**"
        )
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7 
            )
        )

        # ### CRÍTICO 1 ###: Obtener el texto que viene en formato Markdown
        markdown_text = response.text 
        
        # ### CRÍTICO 2 ###: CONVERTIR el Markdown (**) a HTML (<strong>)
        bot_reply = markdown.markdown(markdown_text) # <--- ¡ESTA ES LA SOLUCIÓN!
        
        return JsonResponse({'reply': bot_reply})

    except genai.errors.APIError as e:
        error_message = f"Error de Gemini API: {e}. Revisa tu cuota o clave."
        print(error_message)
        return JsonResponse({'error': 'Lo siento, el asistente IA está experimentando problemas. Revisa tu cuota de uso en Google.'}, status=500)
    
    except Exception as e:
        print(f"Error desconocido al conectar con Gemini: {e}")
        return JsonResponse({'error': 'Error interno del servidor.'}, status=500)


# ------------------------------------------------------------------
# --- VISTA PRINCIPAL ---
# ------------------------------------------------------------------

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
        'featured_repos': data['featured_repos'],
    }
    
    return render(request, 'home.html', context)