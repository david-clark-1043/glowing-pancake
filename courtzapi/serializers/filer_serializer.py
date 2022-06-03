from rest_framework import serializers
from courtzapi.models import Filer
from django.contrib.auth.models import User

from courtzapi.serializers import FilerTypeSerializer
# from courtzapi.serializers.docket_serializer import DocketSerializer

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'is_active', 'date_joined')

class FilerSerializer(serializers.ModelSerializer):
    filer_type = FilerTypeSerializer()
    user = UserSerializer()
    # managing_dockets = DocketSerializer(many=True)
    class Meta:
        model = Filer
        fields = ('id', 'user', 'address_line1', 'address_line2',
                  'address_city', 'state_code', 'zip_code',
                  'phone_num', 'filer_type')
        # not including 'managing_dockets'
        depth = 2
