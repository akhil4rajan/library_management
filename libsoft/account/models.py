from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from oauth2_provider.models import AbstractApplication

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return self.username

class OauthApplication(AbstractApplication):
    pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Function to create Auth Tokens for each User
    """
    if created:
        Token.objects.create(user=instance)