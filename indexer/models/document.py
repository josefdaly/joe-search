from django.db import models

from common.models import TimeStampedModel


class Document(TimeStampedModel):
    url = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    meta = models.TextField(blank=True)
