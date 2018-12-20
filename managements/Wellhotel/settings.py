"""
Django settings for Wellhotel project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'luk9@t3mbrv_jcynh(&hgx+4w*9f1+y%6i5q$e0=gi%wlg=rk%'

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
    'django.contrib.sites',#这边是allauth的依赖包，必须在app和登录模块前面

    'xproject',

    #登录模块
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.github',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wellhotel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "static")],
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

WSGI_APPLICATION = 'Wellhotel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Wellhotel',
        'USER':'sa',
        'PASSWORD':'sa123',
        'HOST':'127.0.0.1',
        'PORT':'1433',
        'OPTIONS':{
            # https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows#using-an-odbc-driver
            'driver': 'ODBC Driver 17 for SQL Server'# SQL Server / SQL Native Client / SQL Server Native Client 10.0 / ODBC Driver 11 for SQL Server
        },
        # 详见：https://docs.djangoproject.com/en/1.11/ref/settings/#conn-max-age
        #数据库连接的生命周期，以秒为单位。用于0在每个请求结束时关闭数据库连接 - Django的历史行为 - 以及 None无限持久连接。默认0
        'CONN_MAX_AGE':None,
    },
}

#使用自己继承的user模型
AUTH_USER_MODEL = "xproject.NormalUser"


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us' # 中文简体:"zh-Hans", 英文:"en-us"

TIME_ZONE = 'Asia/Shanghai' #美国时区:'UTC', 亚洲上海:'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#https://django-allauth.readthedocs.io/en/latest/views.html#login-account-login
###这是allauth基础设置
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = '/'
#登录或者注册成功进入此界面

ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login'
#退出登录后跳转到/accounts/login

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

###这是allauth邮箱设置
ACCOUNT_EMAIL_VERIFICATION = 'optional'
#注册中邮件验证方法 强制（mandatory）”,“可选（optional）”或“否（none）”之一
EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'ma@welltitled.com'
EMAIL_HOST_PASSWORD = 'welldata@123'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'WellData <ma@welltitled.com>'
ACCOUNT_LOGOUT_ON_GET = False
