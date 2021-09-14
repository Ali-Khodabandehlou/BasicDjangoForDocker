# use this command to create superuser
# exec(open('myscript.py').read())

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from ...models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create_user('username', password='password')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        userp = UserProfile(user=user)
        userp.save()
