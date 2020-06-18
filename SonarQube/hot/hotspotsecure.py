# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
from flask import Response

hotspotsecure = "安全热点"
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

@app.route('/')
def index():
    response = Response()
    response.set_cookie('key', 'value') # Sensitive
    return response


str.format(...)
str % str
str + str
f"SELECT * FROM mytable WHERE name = '{value}'"
F"SELECT * FROM mytable WHERE name = '{value}'"

import os

def send_signal(pid, sig, pgid):
    os.kill(pid, sig)  # Sensitive
    os.killpg(pgid, sig)  # Sensitive




import os

value = input()
command = 'os.system("%s")' % value

def evaluate(command, file, mode):
    eval(command)  # Sensitive.

eval(command)  # Sensitive. Dynamic code

def execute(code, file, mode):
    exec(code)  # Sensitive.
    exec(compile(code, file, mode))  # Sensitive.

exec(command)  # Sensitive.