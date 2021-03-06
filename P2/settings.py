"""
Django settings for P2 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf.global_settings import LOGIN_URL

BASE_DIR = Path(__file__).resolve().parent.parent
LOGIN_URL = '/'

REGISTRATION_OPEN = True # 设为 True，允许用户注册
ACCOUNT_ACTIVATION_DAYS = 7  # 留一周的激活时间；当然，也可以设为其他值
# REGISTRATION_AUTO_LOGIN = True   # 设为 True，注册后自动登录
# LOGIN_REDIRECT_URL = '/rango/'   # 登录后呈现给用户的页面

# LOGIN_URL = '/accounts/login/'   # 未登录以及访问需要验证身份的页面时重定向的页面


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e!!q9d20l+uw#1dm!%!w&7ec=xlh3!b)u%-78cm6=fvuwarr($'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'p_general',
    'captcha',
    'rosetta',
    'registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# DENY ：表示该页面不允许在 frame 中展示，即便是在相同域名的页面中嵌套也不允许
# SAMEORIGIN ：表示该页面可以在相同域名页面的 frame 中展示
# ALLOW-FROM uri ：表示该页面可以在指定来源的 frame 中展示
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'P2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/HTML')],
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

WSGI_APPLICATION = 'P2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p2',
        'USER': 'root',
        'PASSWORD': '',  # 123456
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# captacha 验证码
# 使用django-simple-captcha验证码
CAPTCHA_IMAGE_SIZE = (80, 30)  # 设置 captcha 图片大小
CAPTCHA_lENGTH = 4  # 设置字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
# 输入格式：输入框 验证码图片 隐藏域
CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(image)s %(hidden_field)s'
CAPTCHA_NOISE_FUNCTIONS = (
   'captcha.helpers.noise_null',
   'captcha.helpers.noise_arcs',  # 线
   'captcha.helpers.noise_dots',  # 点
)
# 随机字符验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
