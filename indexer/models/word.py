from django.db import models

from common.models import TimeStampedModel


class Word(TimeStampedModel):

    class Meta:
        indexes = [
                models.Index(fields=['text']),
        ]

    text = models.CharField(max_length=255, unique=True)
