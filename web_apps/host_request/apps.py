# Imports
from django.apps import AppConfig


class HostRequestConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'web_apps.host_request'
