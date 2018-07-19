from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class InfoadminConfig(AppConfig):
    name = 'infoadmin'
