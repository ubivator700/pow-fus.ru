# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1744344/data/www/pow-fus.ru/smart')
sys.path.insert(1, '/var/www/u1744344/data/smartenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'smart.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()