from django.contrib import admin

from audit_trail.admin import AuditTrailAdmin
from companies.models import Commerce, Organization


@admin.register(Organization)
class OrganizationAdmin(AuditTrailAdmin):
    pass


@admin.register(Commerce)
class CommerceAdmin(AuditTrailAdmin):
    pass
