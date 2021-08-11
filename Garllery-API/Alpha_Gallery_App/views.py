from django.db import models
from django.shortcuts import render
from rest_framework import generics , viewsets

from .models import Posts , Events , User
from .serializer import PostsSerializer, UserSerializer,EventsSerializer
from django.views.generic.edit import CreateView

# Create your views here.
class PostsListView(generics.ListCreateAPIView):    
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

class PostsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Posts.objects.all()

class EventsListView(generics.ListCreateAPIView):    
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class EventsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UesrListView(generics.ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
    
# class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

# class ArtestsListView(generics.ListCreateAPIView):    
#     serializer_class = ArtestsSerializer
#     queryset = Artests.objects.all()

# class ArtestsDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ArtestsSerializer
#     queryset = Artests.objects.all()

