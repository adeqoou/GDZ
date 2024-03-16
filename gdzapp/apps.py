from django.apps import AppConfig
from .parser import parse_data


class GdzappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gdzapp'

    def ready(self):
        from . import models
        parse_data(models)

