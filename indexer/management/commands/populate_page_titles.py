import requests, re
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand, CommandError

from indexer.models import Document


class Command(BaseCommand):

    def handle(self, *args, **options):
        for doc in Document.objects.all():
            response = requests.get(doc.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content)
                doc.name = soup.title.string
                doc.save()
