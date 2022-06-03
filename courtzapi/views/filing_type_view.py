from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from courtzapi.models import FilingType
from courtzapi.serializers import FilingTypeSerializer


class FilingTypeView(ViewSet):
    def list(self, request):
        """
        GET a list of possible filing type
        """
        filing_type = FilingType.objects.all()
        serializer = FilingTypeSerializer(filing_type, many=True)
        return Response(serializer.data)