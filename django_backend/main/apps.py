from django.apps import AppConfig as BaseAppConfig


class MainConfig(BaseAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
