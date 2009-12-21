#!/usr/bin/env python2.5

import os, re, sys
import getpass

os.environ['AUTH_DOMAIN'] = 'example.com'
os.environ['USER_EMAIL'] = 'test@example.com'

sys.path.append(os.getcwd())
sys.path.append("/home/aldcroft/soft/google_appengine")
sys.path.append("/home/aldcroft/soft/google_appengine/lib/webob")
sys.path.append("/home/aldcroft/soft/google_appengine/lib/yaml/lib")

import models.blog as models

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
    return raw_input('Username:'), getpass.getpass('Password:')

# localhost
# remote_api_stub.ConfigureRemoteDatastore('py4ast', '/remote_api', lambda: ('test@example.com',''), 'localhost:8080')

remote_api_stub.ConfigureRemoteDatastore('py4ast', '/remote_api', auth_func, '0-2-1-tla.latest.py4ast.appspot.com')

for article in db.Query(models.Article).fetch(1000):
    article.title_lower = article.title.lower()
    print article.title_lower
    article.put()
    
    

