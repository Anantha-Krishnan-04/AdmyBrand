from rest_framework import viewsets
from . import models
from . import serializers
#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAuthenticated, IsAdminUser


class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAdminUser]


