import os
import sys

from django.core.wsgi import get_wsgi_application

# --- CORRECCIÓN DE RUTA (SOLUCIÓN DEL ERROR) ---
# Añade el directorio raíz del proyecto al PATH de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
# -------------------------------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analyticsdevs_project.settings')

application = get_wsgi_application()