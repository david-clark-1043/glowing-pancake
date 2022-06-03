from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from courtzapi.models.filers import Filer
from courtzapi.serializers.filer_serializer import FilerSerializer

class FilerView(ViewSet):
    def retrieve(self, request, pk):
        """Get a single filer profile"""
        try:
            filer = Filer.objects.get(pk=pk)
            serializer = FilerSerializer(filer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Filer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)