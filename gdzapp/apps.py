from django.apps import AppConfig
<<<<<<< HEAD
from .parser import parse_data
=======
>>>>>>> e02052c (com2)


class GdzappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gdzapp'
<<<<<<< HEAD

    def ready(self):
        from . import models
        parse_data(models)

=======
>>>>>>> e02052c (com2)
