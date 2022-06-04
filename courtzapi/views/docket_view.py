from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q

from courtzapi.models import Docket
from courtzapi.models.filers import Filer
from courtzapi.serializers import DocketSerializer

class DocketView(ViewSet):
    def list(self, request):
        """
        GET a list of dockets
        """
        filter_filer = request.query_params.get('filer', None)
        if filter_filer is not None:
            filer = Filer.objects.get(pk=filter_filer)
            dockets = Docket.objects.filter(parties__party=filer)
        else:
            dockets = Docket.objects.all()
        
        serializer = DocketSerializer(dockets, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """GET single docket"""
        docket = Docket.objects.get(pk=pk)
        serializer = DocketSerializer(docket)
        return Response(serializer.data, status=status.HTTP_200_OK)