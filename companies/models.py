from uuid import uuid4

from django.db import models

from audit_trail.history import AuditManager, AuditTrail


class Organization(models.Model):
    """Organization model."""

    uuid = models.UUIDField(default=uuid4, primary_key=True)

    nit = models.CharField(max_length=50)
    name = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=100)

    is_active = models.BooleanField(default=False)

    history = AuditTrail()

    objects = AuditManager.as_manager()

    class Meta:
        """Meta options."""
        ordering = ('name',)
        display_format = '{organization}'

    def __str__(self):
        return self.name


class Commerce(models.Model):
    """Commerce model."""

    uuid = models.UUIDField(default=uuid4, primary_key=True)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=120, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    history = AuditTrail()

    objects = AuditManager.as_manager()

    class Meta:
        """Meta options."""
        ordering = ('name',)
        display_format = '{commerce}'
