from rest_framework import serializers

from companies.models import Commerce, Organization
from audit_trail.queries import get_audit_trail


class OrganizationSerializer(serializers.ModelSerializer):
    change_log = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = '__all__'

    def get_change_log(self, obj):
        change_log = get_audit_trail(obj._meta.model_name, obj.pk).values(
            'transacted_on', 'transacted_by',
            'transaction_type', 'field_name',
            'current_val', 'current_val_type',
            'previous_val', 'previous_val_type',
            'xaction__display_text'
        )
        return change_log


class CommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = '__all__'
