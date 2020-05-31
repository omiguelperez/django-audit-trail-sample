from rest_framework import viewsets

from companies.models import Commerce, Organization
from companies.serializers import OrganizationSerializer, CommerceSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class CommerceViewSet(viewsets.ModelViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
