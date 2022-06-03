from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from courtzapi.models import Docket
from courtzapi.models.case_status import CaseStatus
from courtzapi.models.filers import Filer
from courtzapi.serializers import DocketSerializer

class DocketView(ViewSet):
    def list(self, request):
        return ""
    
    def retrieve(self, request, pk):
        """GET single docket"""
        docket = Docket.objects.get(pk=pk)
        serializer = DocketSerializer(docket)
        return Response(serializer.data, status=status.HTTP_200_OK)