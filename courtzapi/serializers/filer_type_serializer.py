from rest_framework import serializers
from courtzapi.models import FilerType


class FilerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilerType
        fields = ('id', 'filer_type')
        depth = 1
