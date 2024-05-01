from django.db import models

from common.models import TimeStampedModel


class DocumentWordIndex(TimeStampedModel):

    class Meta:
        unique_together = ('document', 'word',)

    document = models.ForeignKey('indexer.Document', on_delete=models.CASCADE)
    word = models.ForeignKey('indexer.Word', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
