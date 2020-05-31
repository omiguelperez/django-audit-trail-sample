from django.apps import AppConfig

from audit_trail.signals import audit_m2m_ready, audit_ready


class CompaniesConfig(AppConfig):
    name = 'companies'

    def ready(self):
        audit_ready.send(self.__class__)
        audit_m2m_ready.send(sender=self.__class__)
