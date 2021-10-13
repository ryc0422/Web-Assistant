"""
WSGI config for assistant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
# add your project directory to the sys.path
project_home = u'home/ryc0422/assistant'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set enviroment variable to tell django where your settings.py is
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assistant.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'assistant.settings'



application = get_wsgi_application()
