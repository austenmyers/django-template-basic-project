from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '_media/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# https://docs.djangoproject.com/en/5.1/ref/settings/#static-files
STATIC_ROOT = BASE_DIR / '_media/staticfiles/'
STATIC_URL = '_media/static/'
STATICFILES_DIRS = [
    BASE_DIR / '_media/static/'
]

MEDIA_ROOT = BASE_DIR / '_media/uploads/'
MEDIA_URL = '_media/uploads/'