from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework import viewsets, permissions

from ..utils.permissions import IsUserOrReadOnly
from .models import UserProfile
from .serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        ViewSet for User's model
        permissions: only the user itself and admin users can update this model.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser,
        IsUserOrReadOnly,
    ]

    def get(self):
        return JsonResponse(self.serializer_class.data)

    # todo: create password for the user on create
    def perform_create(self, serializer):
        instance = serializer.save()
        new_profile = UserProfile(user=instance)
        new_profile.save()


class ProfileViewSet(viewsets.ModelViewSet):
    """
        ViewSet for UserProfile's model
        permissions: only the user itself and admin users can update this model.
    """
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [
        # permissions.IsAuthenticated,
        permissions.IsAdminUser,
        IsUserOrReadOnly,
    ]

    def get(self):
        return JsonResponse(self.serializer_class.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
