from rest_framework import serializers
from courtzapi.models import Filing
from courtzapi.serializers import FilerSerializer
from courtzapi.serializers import FilingTypeSerializer
from courtzapi.serializers import DocketSerializer

class FilingSerializer(serializers.ModelSerializer):
    filer = FilerSerializer()
    docket = DocketSerializer()
    filing_type = FilingTypeSerializer()
    class Meta:
        model = Filing
        fields = ('id', 'filer', 'docket', 'docket_index', 'filed_on', 'filing_type', 'file_url')
