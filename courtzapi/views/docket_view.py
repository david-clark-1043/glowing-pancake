from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q
from rest_framework.decorators import action

from courtzapi.models import Docket, CaseStatus
from courtzapi.models.filers import Filer
from courtzapi.serializers import DocketSerializer

class DocketView(ViewSet):
    def list(self, request):
        """
        GET a list of dockets
        """
        filter_filer = request.query_params.get('filer', None)
        filter_open = request.query_params.get('open', None)
        
        if filter_filer is not None:
            filer = Filer.objects.get(pk=filter_filer)
            filer_is_admin = filer.user.is_staff
            if filer_is_admin:
                dockets = Docket.objects.filter(managers=filer)
            else:
                dockets = Docket.objects.filter(parties__party=filer)
        else:
            dockets = Docket.objects.all()
        
        if filter_open is not None:
            dockets = dockets.filter(status_id=1)
        
        serializer = DocketSerializer(dockets, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """GET single docket"""
        docket = Docket.objects.get(pk=pk)
        serializer = DocketSerializer(docket)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['put'], detail=True)
    def close(self, request, pk):
        """ PUT method to close case """
        docket = Docket.objects.get(pk=pk)
        docket.status_id = 2
        docket.closed_on = datetime.now()
        docket.save()
        return Response(None, status=status.HTTP_200_OK)
        
    
    @action(methods=['put'], detail=True)
    def assignManager(self, request, pk):
        """ PUT method to assign managers to a docket """
        docket = Docket.objects.get(pk=pk)
        manager = Filer.objects.get(pk=request.data['manager_id'])
        docket.managers.add(manager)
        return Response({'message': 'Manager Added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def unassignManager(self, request, pk):
        """ DELETE method to remove assigned managers from a docket """
        docket = Docket.objects.get(pk=pk)
        manager = Filer.objects.get(pk=request.data['manager_id'])
        docket.managers.remove(manager)
        return Response({'message': 'Manager Removed'}, status=status.HTTP_201_CREATED)