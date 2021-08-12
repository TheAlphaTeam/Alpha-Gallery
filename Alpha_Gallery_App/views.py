from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny
from django.db import models
from django.shortcuts import render
from rest_framework import generics , viewsets

from .models import Posts , Events , User
from .serializer import PostsSerializer, UserSerializer,EventsSerializer
from django.views.generic.edit import CreateView

# Create your views here.
class PostsListView(viewsets.ModelViewSet):    
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

class PostsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

class EventsListView(viewsets.ModelViewSet):    
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class EventsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


