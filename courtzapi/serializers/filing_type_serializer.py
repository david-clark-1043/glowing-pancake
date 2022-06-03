from rest_framework import serializers
from courtzapi.models import FilingType


class FilingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilingType
        fields = ('id', 'filing_type')
        depth = 1