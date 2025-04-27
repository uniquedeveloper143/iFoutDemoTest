import environ
from pathlib import Path


env = environ.Env()
environ.Env.read_env()

root = environ.Path(__file__) - 3
apps_root = root.path('demo_test')

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY')

# API-KEY Config
# --------------------------------------------------------------------------
API_KEY_SECRET = bytes(env('API_KEY_SECRET'), "utf-8")


# Application definition

DJANGO_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_secure_token',
]


LOCAL_APPS = [
    'demo_test.custom_auth',
    'demo_test.shop',

]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# This is usually the default engine for storing sessions in the database
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ROOT_URLCONF = 'config.urls'

AUTH_USER_MODEL = 'custom_auth.ApplicationUser'

AUTHENTICATION_BACKENDS = (
    'demo_test.custom_auth.auth_backends.model_backend.CustomModelBackend',
)

# Django Rest Framework configurations
# ------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'drf_secure_token.authentication.SecureTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'demo_test.utils.renderer.CustomRenderer'  #you can comment if you want to show restframework ui
    ],
    'PAGE_SIZE': 6,
    'DEFAULT_PAGINATION_CLASS': 'demo_test.utils.paginator.CustomPagination',
}


PROJECT_FULL_NAME = env('PROJECT_FULL_NAME', default='demo_test')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('demo_test', 'templates')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'
STATIC_ROOT = root('static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = [
    root('demo_test', 'assets'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

TITLE_PHOTO_PATH = 'title_image'

# cors
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1',
    'http://127.0.0.1:8000',
    'http://localhost',
    'http://localhost:3000',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*']

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#         'your_app_name': {  # Replace with your actual app name
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#     },
# }

