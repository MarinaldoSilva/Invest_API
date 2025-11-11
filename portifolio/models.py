import uuid

from django.conf import settings
from django.db import models


class Portifolio(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name="portifolio")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    update_in = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} created by {self.owner.username}"