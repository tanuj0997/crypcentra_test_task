from django.apps import AppConfig
from crypcentra.api.signals import create_coin
from crypcentra.api.models import Coins


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        post_save.connect(create_coin, sender=Coins)
