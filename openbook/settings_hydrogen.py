from .settings import *

HYDROGEN_APPS = [
    'hydrogen.apps.HydrogenAppConfig',
]

BASE_URL = 'https://backend.h2pro3.de'
WEBAPP_BASE_URL = 'https://h2pro3.de'

INSTALLED_APPS += HYDROGEN_APPS

GROUP_WEBSITE_MAX_LENGTH = 200
GROUP_POPULATION_MAX_LENGTH = 64
GROUP_AREA_MAX_LENGTH = 100
GROUP_ENERGY_DEMAND_MAX_LENGTH = 40
GROUP_INDUSTRY_MAX_LENGTH = 64
GROUP_EMPLOYEE_MAX_LENGTH = 32
GROUP_LOCATION_MAX_LENGTH = 64
GROUP_INSTITUTION_MAX_LENGTH = 100
GROUP_DEPARTMENT_MAX_LENGTH = 2000
GROUP_PROJECT_DURATION = 64

# firebase credential path
FIREBASE_CREDENTIALS = os.environ.get('FIREBASE_CREDENTIALS')
FIREBASE_CREDENTIALS_PATH = os.environ.get(
    'FIREBASE_CREDENTIALS_PATH',
    os.path.join(BASE_DIR, 'local/h2-firebase-adminsdk.json')
)

# Email Config
EMAIL_SUBJECT_PREFIX = '[H2Pro3] '
DEFAULT_FROM_EMAIL = 'H2Pro3 <noreply_h2pro3@coac.de>'
SERVICE_EMAIL_ADDRESS = 'noreply_h2pro3@coac.de'
SERVER_EMAIL = 'H2Pro3 <noreply_h2pro3@coac.de>'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply_h2pro3@coac.de'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
ADMINS = [('Edison', 'edison.arango@coac.de')]
