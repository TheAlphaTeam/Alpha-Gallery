from django.contrib import admin
from django.urls import path ,include 
from django.conf.urls import url, include
from rest_framework import routers

from .views import EventsListView ,EventsDetailsView ,PostsListView ,PostsDetailsView,UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('posts', PostsListView.as_view(), name ='posts_api'),
    path('events', EventsListView.as_view(), name ='events_api'),
    path('posts/<int:pk>/', PostsDetailsView.as_view(), name ='posts_details'),
    path('events/<int:pk>/', EventsDetailsView.as_view(), name ='events_details'),
    url(r'^', include(router.urls)),
]

    
    