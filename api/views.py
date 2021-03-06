from django.db.models import query
from api.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from api import serializers
from api import models
from api import permissions
# Create your views here.

class User(APIView):
    serializers_class = serializers.UserSerializer

    def get(self, request, format=None):
        return Response({'message': 'Hello World!'})

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})


class UserViewSet(viewsets.ViewSet):
    serializers_class = serializers.UserSerializer

    def list(self, request):
        res = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'Automatically maps URLS using Routers',
            'Provides more funcs with less code'
        ]

        return Response({'message': 'Hello!', 'res': res})

    def create(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'get'})

    def update(self, request, pk=None):
        return Response({'method': 'put'})

    def partial_update(self, request, pk=None):
        return Response({'method': 'patch'})

    def destroy(self, request, pj=None):
        return Response({'method': 'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')

class UserLoginApiView(ObtainAuthToken): 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
            