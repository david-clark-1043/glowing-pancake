from rest_framework import serializers
from courtzapi.models import PartyType


class PartyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyType
        fields = ('id', 'party_type')
        depth = 1