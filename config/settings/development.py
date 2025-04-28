from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1', ]

ADMINS = (
    ('Dev Email', env('DEV_ADMIN_EMAIL', default='nafees.mohd@neosoftmail.com')),
)

MANAGERS = ADMINS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': Path(__file__).resolve().parent.parent / 'db.sqlite3',
#     }
# }


# print("env('DB_NAME')", env('DB_NAME'))
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# E-mail settings
# -----------------------------------------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Use your email provider's SMTP server
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') # app password without space

# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = SERVER_EMAIL = env('SERVER_EMAIL_SIGNATURE') + ' <%s>' % env('SERVER_EMAIL')


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025  # MailHog's default SMTP port
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False

