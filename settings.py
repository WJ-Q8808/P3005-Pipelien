# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
DATABASES = {
    'postgresql_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quickdb',
        'USER': 'sonarsource',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

def get_databases_user_password(databases_settings):
    databases_key = databases_settings.keys()
    databases_value = databases_settings.values()
    print(databases_key,databases_value)
    return