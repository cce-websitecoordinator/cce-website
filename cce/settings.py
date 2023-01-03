import os
from pickle import FALSE
import shutil
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#setting up environment variables
env = environ.Env()
environ.Env.read_env()

# setting up environment variables
env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'departments',
    'aboutCCE',
    'Administration',
    'StudentServices',
    'storages',

    # 'tailwind', // activate this in production to use Tailwind CSS
    # 'theme'

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]


# Development Settings

if env('PRODUCTION') != 'True':
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
    INSTALLED_APPS.append("django_browser_reload")
    DEBUG = True


ROOT_URLCONF = 'cce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'cce.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Added by manually
# custom settings
if env('PRODUCTION') != 'True':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
INTERNAL_IPS = [
    "127.0.0.1",
]

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'cce-website-media'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
# MEDIA_URL = S3_URL + MEDIA_ROOT
DEFAULT_FILE_STORAGE = 'cce.storage_backends.MediaStorage'


# Jazzmin settings

JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
    "dark_mode_theme": "cerulean",
}


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "CCE Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "CCE",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "CCE",

    # # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "favicons/favicon-32x32.png",
    "site_logo_small": "favicons/favicon-32x32.png",

    "site_favicon": "favicons/favicon.ico",
     "login_logo": "favicons/android-chrome-192x192.png",


    # # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    # "site_icon": None,

    # # Welcome text on the login screen
    "welcome_sign": "Welcome Administration Page of CCE Web",

    # # Copyright on the footer
    "copyright": " Christ College Of Engineering & Technology",



    # # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"Main Website": "website"},
        {"Departments": "departments"},
    ],

    "related_modal_active": True,
}


