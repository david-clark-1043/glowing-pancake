from rest_framework import serializers

from courtzapi.models import Firm

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'name', 'representatives')
