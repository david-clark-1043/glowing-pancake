from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from courtzapi.models import PartyType
from courtzapi.serializers import PartyTypeSerializer


class PartyTypeView(ViewSet):
    def list(self, request):
        """
        GET a list of possible party types
        """
        party_type = PartyType.objects.all()
        serializer = PartyTypeSerializer(party_type, many=True)
        return Response(serializer.data)