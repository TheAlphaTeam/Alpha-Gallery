from django.contrib import admin
from django.urls import path ,include 
from django.conf.urls import url, include
from rest_framework import routers

from .views import EventsListView ,EventsDetailsView ,PostsListView ,PostsDetailsView,UserViewSet, CurrentUserView

router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router3 = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router1.register(r'posts', PostsListView)
router2.register(r'events', EventsListView)

urlpatterns = [
    path('current', CurrentUserView.as_view(), name ='current-user'),
    # path('events', EventsListView.as_view(), name ='events_api'),
    # path('posts/<int:pk>/', PostsDetailsView.as_view(), name ='posts_details'),
    # path('events/<int:pk>/', EventsDetailsView.as_view(), name ='events_details'),
    url(r'^', include(router.urls)),
    url(r'^', include(router1.urls)),
    url(r'^', include(router2.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]

    
    