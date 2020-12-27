"""
WSGI config for _djreact2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# from whitenoise.django import DjangoWhiteNoise 
#  ДАЕТ ОШИБКУ  django.core.exceptions.ImproperlyConfigured: WSGI application '_djreact2.wsgi.application' could not be loaded; Error importing module.
# http://whitenoise.evans.io/en/stable/changelog.html#v4-0


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_djreact2.settings')

application = get_wsgi_application()

