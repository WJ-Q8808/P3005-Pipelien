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

def get_databases(databases_settings):
    databases_key = databases_settings.keys()
    databases_value = databases_settings.values()
    databases_item = databases_settings.items()
    print(databases_key)
    print(databases_value)
    return databases_key

def get_data(databases_settings):
    databases_key = databases_settings.keys()
    databases_value = databases_settings.values()
    databases_item = databases_settings.items()
    print(databases_key)
    print(databases_value)
    return databases_key,databases_value

def get_databas(databases_settings):
    databases_key = databases_settings.keys()
    databases_value = databases_settings.values()
    databases_item = databases_settings.items()
    print(databases_key)
    print(databases_value)
    return databases_key,databases_value

import ssl

ctx = ssl._create_unverified_context() # Noncompliant: by default hostname verification is not done
ctx = ssl._create_stdlib_context() # Noncompliant: by default hostname verification is not done

ctx = ssl.create_default_context()
ctx.check_hostname = False # Noncompliant

ctx = ssl._create_default_https_context()
ctx.check_hostname = False # Noncompliant