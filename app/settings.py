import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'cin2c^lk79t6p$msc^f(lp1o2lp@9n4u!5odr(_h2hor*dqnrc'

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    '167.172.182.37'
]
SCHEMA = 'http'
M_HOST = '167.172.182.37:8000'
MAIN_HOST = 'http://167.172.182.37:8000'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'core',
    'shop',
    'cart',
    'order',
    'customer'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'shop', 'templates'),
            os.path.join(BASE_DIR, 'cart', 'templates'),
            os.path.join(BASE_DIR, 'order', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'core.context_processors.config',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '',
        'PORT': '',
        'NAME': 'cornelius',
        'USER': 'cornelius_db',
        'PASSWORD': 'Qz314159',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hekto.v8@gmail.com'
EMAIL_HOST_PASSWORD = 'Qz314159'

EMAIL_CORNELIUS = 'lutogin@gmail.com'
EMAIL_ADMIN = 'lutogin+admin@gmail.com'

RECAPTCHA_PUBLIC_KEY = '6LdsyroUAAAAAAR278Z5cZECjTqH25FtYJbIJ0Ju'
RECAPTCHA_PRIVATE_KEY = '6LdsyroUAAAAACJDwqEzAIfzzkxw9T0O_0rQ9RFf'
# RECAPTCHA_PROXY = {'http': 'http://127.0.0.1:8000', 'https': 'https://127.0.0.1:8000'}
RECAPTCHA_DOMAIN = 'www.recaptcha.net'

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

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
   }
}

MIDDLEWARE += [
   'django.middleware.cache.UpdateCacheMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.cache.FetchFromCacheMiddleware',
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AUTH_USER_MODEL = 'core.User'

CART_SESSION_ID = 'cart'

PYTHONHTTPSVERIFY = 0
