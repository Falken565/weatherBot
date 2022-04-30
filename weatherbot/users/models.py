from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    status = models.BooleanField(default=False)
    tg_id = models.IntegerField(blank=True, null=True)
