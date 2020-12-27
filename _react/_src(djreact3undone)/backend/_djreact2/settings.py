import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'uff*9)0z68iipr!3&9ijt5$w*m8m*nqxqq!q)ifu7xk!4czmnb'

DEBUG = True

ALLOWED_HOSTS = [
    'justdjango-react-django-app-2.herokuapp.com',
    'localhost',
    '127.0.0.1',
    ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    # нужно для того, чтобы у fetch из js был доступ к данным которые передаются через django-api, и браузер не ругался на CORS-запреты
    'corsheaders',
    'rest_framework',
    'whitenoise',
]

MIDDLEWARE = [
    # нужно для того, чтобы у fetch из js был доступ к данным которые передаются через django-api, и браузер не ругался на CORS-запреты
    'corsheaders.middleware.CorsMiddleware',

    # нужен для обработки статики при деплое на хероку
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# нужно для того, чтобы у fetch из js был доступ к данным которые передаются через django-api, и браузер не ругался на CORS-запреты. Также можно отдельно указать домены, у которых будет доступ к апи, а остальные заблочить
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = '_djreact2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # нужно для того, чтобы можно было иметь доступ к фронтэнду без запуска веб-сервера через npm run start => localhost:3000.
            # Можно просто запустить python src/backend/manage.py runserver => localhost:8000
            # Но для этого надо еще добавить в urls re_path('.*', TemplateView.as_vew(template_name='index.html'))
            os.path.join(
                os.path.dirname(
                    os.path.dirname(BASE_DIR)
                ), 'build'
            )
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


WSGI_APPLICATION = '_djreact2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(
        os.path.dirname(
            os.path.dirname(BASE_DIR)
        ), 'build/static'
    )
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.AllowAny',
    ]
}

# нужно для деплоя на хероку
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# нужно для того чтобы укзаать как whitenoise будет хранить статические файлы
# STATICFILES_STOGARE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STOGARE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
