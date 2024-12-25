"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-eh!78m07+#_4nhy$a(v67kxh_e%%^9opf)3*w7^&##8fki6e+&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


# Application definition

INSTALLED_APPS = [
    "unfold",
    'corsheaders',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # install apps
    'rest_framework',
    'django_core',
    
    # other apps
    'users',
    'api',
    'basket',
    'product',
    'order'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# unfold solf

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "ASADMAXMUD",
    "SITE_HEADER": "ASADMAXMUD",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_LOGO": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_SYMBOL": "speed",  # Symbol from the icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",  # Updated to PNG for better compatibility
            "href": lambda request: static("logo/favicon.png"),
        },
    ],
    "SHOW_HISTORY": True,  # Show/hide the "History" button
    "SHOW_VIEW_ON_SITE": True,  # Show/hide the "View on site" button
    "ENVIRONMENT": None,
    "DASHBOARD_CALLBACK": None,
    "STYLES": [
        lambda request: static("css/style.css"),  # Custom styles
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),  # Custom scripts
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
    "show_search": True,  # Enable search in applications and models names
    "show_all_applications": True,  # Dropdown with all applications and models
    "navigation": [
        {
            "title": _("Asosiy Sahifa"),
            "separator": False,  # Top border
            "items": [
                {
                    "title": _("Asosiy sahifa"),
                    "icon": "home",
                    "link": reverse_lazy("admin:index"),
                },
                {
                    "title": _("Foydalanuvchilar"),
                    "icon": "person",
                    "link": reverse_lazy("admin:users_usermodel_changelist"),
                },
            ],
        },
        {
            "title": _("Mahsulot va Kategoryalar"),
            "separator": True,
            "collapsible": True,  
            "items": [
                {
                    "title": _("Mahsulotlar"),
                    "icon": "inventory",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:product_productmodel_changelist"),
                },
                {
                    "title": _("Kategoryalar"),
                    "icon": "category",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:product_categorymodel_changelist"),
                },
            ],
        },
        {
            "title": _("Qo'shimcha Elementlar"),
            "separator": True,
            "collapsible": True,  
            "items": [
                {
                    "title": _("Mahsulot rangi"),
                    "icon": "palette",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:product_colormodel_changelist"),
                },
                {
                    "title": _("Mahsulot o'lchami"),
                    "icon": "straighten",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:product_sizemodel_changelist"),
                },
            ],
        },
        {
            "title": _("Savat va Buyurtmalar"),
            "separator": True,
            "collapsible": True,  
            "items": [
                {
                    "title": _("Savatcha"),
                    "icon": "shopping_cart",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:basket_cartmodel_changelist"),
                },
                {
                    "title": _("Savat Buyumlar"),
                    "icon": "shopping_cart",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:basket_cartitemmodel_changelist"),
                },
                {
                    "title": _("Buyurtmalar"),
                    "icon": "receipt_long",  # Django Unfold ikonkasi
                    "link": reverse_lazy("admin:order_ordermodel_changelist"),
                },
            ],
        },
    ],
},

}


