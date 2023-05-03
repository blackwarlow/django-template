from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
SECRET_KEY = "django-insecure-p5ir9_mi)un&m&+n0)@hujc_plpz$_+tg1%%9v4x!(7iiv&gi)"

DEBUG = True

ALLOWED_HOSTS = ["localhost"]

INSTALLED_APPS = [
    "baton",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "baton.autodiscover",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Whitenoise static serve
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
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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
AUTH_USER_MODEL = "main.User"

# I18N, L10N, TZ for Moscow
LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "Etc/GMT-3"

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Whitenoise serve settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

BATON = {
    "SITE_HEADER": "Template",
    "SITE_TITLE": "Template",
    "INDEX_TITLE": "Site administration",
    "SUPPORT_HREF": "https://github.com/blackwarlow/",
    "COPYRIGHT": 'copyright © 2023 <a href="https://github.com/blackwarlow/">Blackwarlow</a>',  # noqa
    "POWERED_BY": '<a href="https://www.otto.to.it">Otto srl</a>',
    "CONFIRM_UNSAVED_CHANGES": True,
    "SHOW_MULTIPART_UPLOADING": True,
    "ENABLE_IMAGES_PREVIEW": True,
    "CHANGELIST_FILTERS_IN_MODAL": True,
    "CHANGELIST_FILTERS_ALWAYS_OPEN": False,
    "CHANGELIST_FILTERS_FORM": True,
    "COLLAPSABLE_USER_AREA": False,
    "MENU_ALWAYS_COLLAPSED": False,
    "MENU_TITLE": "Menu",
    "MESSAGES_TOASTS": False,
    "GRAVATAR_DEFAULT_IMG": "retro",
    "GRAVATAR_ENABLED": True,
    "LOGIN_SPLASH": "/static/core/img/login-splash.png",
    "SEARCH_FIELD": {
        "label": "Search...",
        "url": "/search/",
    },
    "MENU": (
        {
            "type": "free",
            "label": "Authentication",
            "icon": "fa fa-lock",
            "default_open": True,
            "children": (
                {
                    "type": "model",
                    "label": "Users",
                    "name": "user",
                    "app": "main",
                    "icon": "fa fa-user",
                },
                {
                    "type": "model",
                    "label": "Groups",
                    "name": "group",
                    "app": "auth",
                    "icon": "fa fa-users",
                },
            ),
        },
        {
            "type": "free",
            "label": "Menu item",
            "children": [
                {"type": "free", "label": "Google", "url": "http://google.com"},
            ],
        },
    ),
    "ANALYTICS": None,
}
