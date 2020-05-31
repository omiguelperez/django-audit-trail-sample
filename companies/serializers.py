from rest_framework import serializers

from companies.models import Commerce, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class CommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = '__all__'
