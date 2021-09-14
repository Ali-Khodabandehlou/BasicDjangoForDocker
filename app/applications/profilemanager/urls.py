from django.urls import path, include

from rest_framework import routers

from .views import UserViewSet, ProfileViewSet

app_name = 'profilemanager'

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='listusers')
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
