from django.apps import AppConfig


class HydrogenAppConfig(AppConfig):
    name = 'hydrogen'

    def ready(self):
        # Load the signals
        import hydrogen.signals
