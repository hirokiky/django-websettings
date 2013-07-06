from django.conf import settings
from django.utils.importlib import import_module

from websettings.backends import db as db_backend

try:
    backend_path = settings.WEBSETTINGS_BACKEND
    backend_module = import_module(backend_path)
except (AttributeError, TypeError, ImportError):
    backend_module = db_backend


