import requests
import os # Asegúrate de importar os
from django.shortcuts import render

# ... (La función get_language_color permanece igual) ...

# ====================================================================
# CONFIGURACIÓN DE GITHUB
# ====================================================================
GITHUB_USERNAME = "GeraMartinez94"
# Obtener el token de la variable de entorno GITHUB_PAT
# FORZANDO LA CONEXIÓN: Token directo
GITHUB_TOKEN = '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'
# ====================================================================

# ... (El resto de tus funciones get_github_data y home_view permanecen iguales) ...
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
    """Obtiene lenguajes y la lista de repositorios fijados (pinned)."""
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 1. Obtener TODOS los repositorios para el cálculo de lenguajes
    repos_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?type=owner"
    
    try:
        response = requests.get(repos_url, headers=headers)
        response.raise_for_status()
        repos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error crítico al obtener repositorios: {e}")
        return {'languages': [], 'featured_repos': []} 

    # --- Lógica de Lenguajes (se mantiene igual) ---
    total_bytes = 0
    language_totals = {}
    
    # Lista para almacenar solo los datos relevantes para los repos fijados.
    all_repo_data = {} 

    for repo in repos:
        if repo.get('fork'):
            continue
            
        # Almacenamos los datos clave de todos los repositorios para luego filtrar los fijados.
        all_repo_data[repo['name']] = {
            'name': repo.get('name'),
            'description': repo.get('description') or "Sin descripción.",
            'html_url': repo.get('html_url'),
            'language': repo.get('language'), 
            'updated_at': repo.get('updated_at')
        }

        # Acumular lenguajes por bytes
        languages_url = repo['languages_url']
        try:
            lang_response = requests.get(languages_url, headers=headers)
            lang_response.raise_for_status()
            languages = lang_response.json()
            
            for lang, bytes_count in languages.items():
                language_totals[lang] = language_totals.get(lang, 0) + bytes_count
                total_bytes += bytes_count
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener lenguajes del repo {repo.get('name', 'N/A')}: {e}")
            continue
    # ------------------------------------------------

    # 2. Calcular porcentajes de lenguajes (queda igual)
    language_percentages = []
    if total_bytes > 0:
        sorted_languages = sorted(language_totals.items(), key=lambda item: item[1], reverse=True)
        for lang, bytes_count in sorted_languages:
            percent = (bytes_count / total_bytes) * 100
            language_percentages.append({
                'language': lang,
                'percent': round(percent, 2),
                'color': get_language_color(lang)
            })

    # 3. Obtener la lista de los 4 repositorios FIJADOS (Pinned)
    #    Utilizaremos un endpoint que a veces contiene metadata de los repos fijados en la respuesta de usuario
    #    o simplemente usaremos los nombres que vimos en tu perfil:
    
    # Nombres basados en tu captura de pantalla (image_9d9def.png)
    pinned_repo_names = [
        "Reconocimiento_gestos_Python", 
        "Scrapting_Python", 
        "Data-Analytics-Python", 
        "Project_graphic_python"
    ]
    
    # Filtramos los datos completos de los repositorios para obtener solo los fijados
    featured_repos = [all_repo_data[name] for name in pinned_repo_names if name in all_repo_data]
    
    return {
        'languages': language_percentages[:5],
        'featured_repos': featured_repos, 
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
        'featured_repos': data['featured_repos'],
    }
    
    return render(request, 'home.html', context)
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
        'featured_repos': data['featured_repos'], # <--- NUEVO CONTEXTO AGREGADO
    }
    
    return render(request, 'home.html', context)
    """Vista principal que renderiza la página y pasa los datos de GitHub."""
    
    languages = get_github_languages()
    
    # Prepara los datos para el conic-gradient de CSS
    current_stop = 0
    gradient_parts = []
    for lang in languages:
        next_stop = current_stop + lang['percent']
        # Formato CSS: COLOR START% END%
        gradient_parts.append(f"{lang['color']} {current_stop:.2f}% {next_stop:.2f}%")
        current_stop = next_stop

    gradient_string = ", ".join(gradient_parts)
    
    context = {
        'languages': languages,
        'gradient_string': gradient_string,
    }
    
    # ⚠️ Solución al error TemplateDoesNotExist: Asegura que 'home.html' exista
    try:
        get_template('home.html')
    except Exception as e:
        # Esto te mostrará en la consola si el error persiste a pesar de la corrección
        print(f"ADVERTENCIA: Aún no se encuentra la plantilla home.html. Error original: {e}") 

    return render(request, 'home.html', context)