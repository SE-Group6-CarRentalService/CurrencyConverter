from django.apps import AppConfig

class SoapserviceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "SOAPservice"
    
    def ready(self):
        from . import updater
        updater.start()
