import hashlib
import os
import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ..utils.models import Base


# defining default settings
AVATAR_DIRECTORY = 'avtr'
DEFAULT_PROFILE_IMG = os.path.join(AVATAR_DIRECTORY, 'profile.png')

def avatar_path(instance, filename):
    """
    Encrypts filename of uploaded image with sha256 method.
    """
    file_name, file_ext = os.path.splitext(filename)
    file_name = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    filename = ''.join([file_name, file_ext])
    return '/'.join([AVATAR_DIRECTORY, filename])


class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_photo = models.ImageField(upload_to=avatar_path, default=DEFAULT_PROFILE_IMG)
    
    def __str__(self):
        return self.user.username

    # returns profile photo url
    @property
    def show_avatar(self):
        return self.profile_photo.url if self.profile_photo else DEFAULT_PROFILE_IMG

