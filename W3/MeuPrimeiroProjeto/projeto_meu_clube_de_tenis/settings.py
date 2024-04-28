"""
Configurações do Django para o projeto projeto_meu_clube_de_tenis.

Gerado por 'django-admin startproject' usando Django 5.0.4.

Para mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/5.0/topics/settings/

Para a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Construa caminhos dentro do projeto assim: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações de desenvolvimento rápido - inadequadas para produção
# Consulte https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# AVISO DE SEGURANÇA: mantenha a chave secreta usada em produção em segredo!
SECRET_KEY = "django-insecure-2a!%45tq13o1p+=_yweij-tvovcy3d2h25+!ho=o(e)4fk*-39"

# AVISO DE SEGURANÇA: não execute com debug ativado em produção!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Definição de aplicativos

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "appmembers",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "projeto_meu_clube_de_tenis.urls"

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

WSGI_APPLICATION = "projeto_meu_clube_de_tenis.wsgi.application"


# Banco de dados
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Validação de senhas
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internacionalização
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Tipo de campo de chave primária padrão
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
