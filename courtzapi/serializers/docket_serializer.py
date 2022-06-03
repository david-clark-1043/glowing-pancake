from rest_framework import serializers
from courtzapi.models import Docket
from courtzapi.serializers import CaseStatusSerializer
from courtzapi.serializers import FilerSerializer

class DocketSerializer(serializers.ModelSerializer):
    status = CaseStatusSerializer()
    managers = FilerSerializer(many=True)
    class Meta:
        model = Docket
        fields = ("id", "case_num", "status", "created_on", "completed_on", "managers")
        depth = 2
