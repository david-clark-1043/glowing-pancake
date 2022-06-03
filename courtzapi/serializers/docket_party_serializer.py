from rest_framework import serializers
from courtzapi.models import DocketParty
from courtzapi.serializers import FilerSerializer
from courtzapi.serializers import DocketSerializer
from courtzapi.serializers import PartyTypeSerializer

class DocketPartySerializer(serializers.ModelSerializer):
    party = FilerSerializer()
    docket = DocketSerializer()
    party_type = PartyTypeSerializer()
    class Meta:
        model = DocketParty
        fields = ('id', 'party', 'docket', 'party_type')
