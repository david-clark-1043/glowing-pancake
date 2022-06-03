from rest_framework import serializers
from courtzapi.models import Filer
from courtzapi.serializers import FilerTypeSerializer
from courtzapi.serializers import DocketSerializer

class FilerSerializer(serializers.ModelSerializer):
    filer_type = FilerTypeSerializer()
    managing_dockets = DocketSerializer(many=True)
    class Meta:
        model = Filer
        fields = ('id', 'user', 'address_line1', 'address_line2',
                  'address_city', 'state_code', 'zip_code',
                  'phone_num', 'filer_type', 'managing_dockets')
        depth = 2
