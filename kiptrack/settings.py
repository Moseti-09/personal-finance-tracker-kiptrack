# At the top with other imports
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# ... existing BASE_DIR etc.

SECRET_KEY = 'django-insecure-your-key-here'

DEBUG = True

ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'finances.apps.FinancesConfig', 
     
]

# ... other settings ...

LOGIN_REDIRECT_URL = 'dashboard'       # after login go here
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

ROOT_URLCONF = 'kiptrack.urls'
# If not already present
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ← make sure this line exists
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',     # ← might be missing
                'django.contrib.auth.context_processors.auth',    # ← might be missing
                'django.contrib.messages.context_processors.messages',  # ← might be missing
            ],
        },
    },
]

STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']   # add later if you use local CSS/JS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',          # must be here
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',       # must be after SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',          # must be after auth
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}