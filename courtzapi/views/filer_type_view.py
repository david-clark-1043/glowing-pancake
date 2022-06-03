from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from courtzapi.models import FilerType
from courtzapi.serializers import FilerTypeSerializer


class FilerTypeView(ViewSet):
    def list(self, request):
        """
        GET a list of possible filer types
        """
        filer_type = FilerType.objects.all()
        serializer = FilerTypeSerializer(filer_type, many=True)
        return Response(serializer.data)