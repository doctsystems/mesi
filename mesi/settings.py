import os
from decouple import config, Csv
from dj_database_url import parse as db_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'app',
    'pde',
    'django_userforeignkey',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_userforeignkey.middleware.UserForeignKeyMiddleware',
]

ROOT_URLCONF = 'mesi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mesi.wsgi.application'

DATABASES = {
    'default': config('DATABASE_URL_1', cast=db_url),
    'iiep': config('DATABASE_URL_2', cast=db_url),
}
DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['iiep']['ENGINE'] = 'django.db.backends.mysql'

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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/admin/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')

JAZZMIN_SETTINGS = {
    'site_title': 'MESI',
    'site_header': 'MESI',
    'site_logo': 'core/img/logo.jpg',
    'welcome_sign': 'Bienvenido a MESI',
    'copyright': 'MESI - IIEP',
    'search_model': 'app.publicacion',
    'user_avatar': None,

    # Top Menu #
    'topmenu_links': [
        {'name': 'VER SITIO WEB',  'url': 'core:home',},
        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        # {'model': 'auth.User'},
        # {'app': 'app'},
    ],

    # User Menu #
    'usermenu_links': [
        {'name': 'Ayuda', 'url': 'https://twitter.com/diegocruztorrez', 'new_window': True},
        # {'model': 'auth.user'}
    ],

    # Side Menu #
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    # 'hide_models': ['dashboard.departamento', 'dashboard.municipio',],
    'order_with_respect_to': ['app', 'accounts'],
    'custom_links': {
        # 'app': [{
        #     'name': 'Cerrar Sesion', 
        #     'url': 'core:logout',
        #     'icon': 'fas fa-sign-out-alt',
        # }]
    },

    # Iconos personalizados para el menu de apps/models - https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    'icons': {
        'auth': 'fas fa-user',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',

        'app.actividad': 'fab fa-delicious',
        'app.investigador': 'fas fa-user-tie',
        'app.novedad': 'fas fa-newspaper',
        'app.proyecto': 'fas fa-business-time',
        'app.publicacion': 'fab fa-diaspora',
    },

    # Iconos que se usan cuando no se especifica uno manualmente
    'default_icon_parents': 'fab fa-diaspora',
    'default_icon_children': 'fas fa-question',

    # UI Tweaks #
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": 'app/css/custom_ckeditor.css',
    "custom_js": None,
    "show_ui_builder": False,

    # Change view #
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-lightblue",
    "navbar": "navbar-lightblue navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-lightblue",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}
