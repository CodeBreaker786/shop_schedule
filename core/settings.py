import os
from pathlib import Path
 

 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL_LIBRARY_PATH = '/System/Volumes/Data/usr/local/Cellar/gdal/3.5.1_2/lib/libgdal.dylib'
# GEOS_LIBRARY_PATH = '/System/Volumes/Data/usr/local/Cellar/geos/3.11.0/lib/libgeos_c.1.17.0.dylib'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
# GEOS_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgeos_c.so' if os.environ.get('ENV') == 'HEROKU' else os.getenv('GEOS_LIBRARY_PATH')
# GDAL_LIBRARY_PATH = '/app/.heroku/vendor/lib/libgdal.so' if os.environ.get('ENV') == 'HEROKU' else os.getenv('GDAL_LIBRARY_PATH')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ="django-insecure-iz9=0_96x_ua-u9zt86^*u(645x-z5j&4h*loj5a6!j!=60w&y"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'rest_framework',
    'shops',
   
  
    
    
    
    

    
    


]
SITE_ID = 1
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'utils.exception_handle.ExceptionMiddleware'
]


AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
 
   
 
)
 
ROOT_URLCONF = 'core.urls'
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

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.exception_handle.handle_exception',
    'DEFAULT_RENDERER_CLASSES': [
        'utils.json_response_renderer.MyJsonRenderer',
        
        
    ],
 
    'COERCE_DECIMAL_TO_STRING': False,
   
   
}

 
    

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# STATIC_URL = 'static/'
 

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 


 

 