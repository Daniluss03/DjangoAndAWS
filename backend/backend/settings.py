
from pathlib import Path
from decouple import config 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nqf5$0sze93ufa#mf3*ymhyo5zt)3vnh6#ea@rsrr29wbj_y(p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.daniluss.com','daniluss.com','*']
CSRF_TRUSTED_ORIGINS = ['https://www.daniluss.com','https://daniluss.com']





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'continousintegrationanddelivery',
    'crispy_forms',
    'storages',
]

CRISPY_TEMPLATE_PACK='bootstrap4'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':config('NAME_DATABASE'),
        'USER':config('NAME_USER_DATABASE')  ,
        'PASSWORD':config('PASSWORD_DATABASE') , 
        'HOST':config('HOST') ,
        'PORT':config('PORT')
    }
}

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
#desarollo
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR / 'static/images'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')  
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')  
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')  

#producción

STORAGES = {

    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",        
    },

    "staticfiles":
    {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
     
     }


}

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False


# ses configuration
EMAIL_BACKEND='django_ses.SESBackend'

AWS_SES_REGION_NAME='us-east-1'

AWS_SES_REGION_ENDPOINT='email.us-east-1.amazonaws.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'  
EMAIL_PORT = config('EMAIL_PORT') 
EMAIL_USE_TLS = config('EMAIL_USE_TLS')  
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')  



