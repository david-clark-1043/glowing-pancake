from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from courtzapi.models.filer_type import FilerType


from courtzapi.models.filers import Filer
from courtzapi.serializers import FilerSerializer, UpdateFilerSerializer, UserSerializer

class FilerView(ViewSet):
    def retrieve(self, request, pk):
        """Get a single filer profile"""
        try:
            filer = Filer.objects.get(pk=pk)
            serializer = FilerSerializer(filer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Filer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """ GET all filers """
        filers = Filer.objects.all()
        serializer = FilerSerializer(filers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        filer = Filer.objects.get(pk=pk)
        user = User.objects.get(pk=pk)
        filer_type = FilerType.objects.get(pk=request.data["filer_type_id"])
        updated_user = {
            "username": request.data['username'],
            "email": request.data['email'],
            "first_name": request.data['first_name'],
            "last_name": request.data['last_name']
        }
        
        user_serializer = UserSerializer(user, data=updated_user)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        user.refresh_from_db()
        
        updated_filer = {
            "address_line1": request.data['address_line1'],
            "address_line2": request.data['address_line2'],
            "address_city": request.data['address_city'],
            "state_code": request.data['state_code'],
            "zip_code": request.data['zip_code'],
            "phone_num": request.data['phone_num']
        }
        filer_serializer = UpdateFilerSerializer(filer, data=updated_filer)
        filer_serializer.is_valid(raise_exception=True)
        filer_serializer.save(filer_type=filer_type, user=user)
        return Response(None, status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=False)
    def admins(self, request):
        filers = Filer.objects.filter(user__is_staff=True)
        serializer = FilerSerializer(filers, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({'message': "User deactivated"}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def activate(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response({'message': "User activated"}, status=status.HTTP_201_CREATED)
    
    @action(methods=['put'], detail=True)
    def promoteAdmin(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = True
        user.save()
        return Response({'message': "Admin added"}, status=status.HTTP_201_CREATED)
    
    @action(methods=['put'], detail=True)
    def demoteAdmin(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = False
        user.save()
        return Response({'message': "Admin removed"}, status=status.HTTP_201_CREATED)