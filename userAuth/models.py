import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Counter(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(null=True, blank=True, max_length=100)
    value = models.BigIntegerField()

    def __str__(self):
        return self.key