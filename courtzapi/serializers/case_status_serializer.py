from rest_framework import serializers
from courtzapi.models import CaseStatus


class CaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStatus
        fields = ('id', 'status_label')
        depth = 1
