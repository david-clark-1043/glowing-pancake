from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from courtzapi.models import CaseStatus
from courtzapi.serializers import CaseStatusSerializer


class CaseStatusView(ViewSet):
    def list(self, request):
        """
        GET a list of possible case statuses
        """
        case_status = CaseStatus.objects.all()
        serializer = CaseStatusSerializer(case_status, many=True)
        return Response(serializer.data)