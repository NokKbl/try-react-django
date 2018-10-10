import os

from django.core.wsgi import get_wsgi_apllication
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
"DjangoReact.settings")

application = get_wsgi_apllication()
application = DjangoWhiteNoise(application)
