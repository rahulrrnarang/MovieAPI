import uuid

from django.db import models

class Collection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title