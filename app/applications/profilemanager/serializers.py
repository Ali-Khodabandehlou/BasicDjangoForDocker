from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from rest_framework import serializers

from .models import UserProfile


# todo: complete these serializers
class ProfileSerializer(serializers.ModelSerializer):
    """
    serializer for the UserProfile model
    """
    user = serializers.CharField(source='user.username')

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'profile_photo',
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for the django's User models
    """
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        ]
