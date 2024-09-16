from django.apps import AppConfig


class InvisibleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invisible'
