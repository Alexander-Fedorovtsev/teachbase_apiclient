from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    externalid = models.CharField(max_length=25, null=True, blank=True)
    accesstoken = models.CharField(max_length=50, null=True, blank=True)


def __str__(self):
    return str(self.user)
