import requests, json, urllib

from django.core.management.base import BaseCommand, CommandError

from indexer.models import Document


class Command(BaseCommand):

    def handle(self, *args, **options):
        url_template = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={}'
        for doc in Document.objects.all():
            if doc.name:
                url = url_template.format(doc.url.split('/')[-1])
                response = requests.get(url)
                if response.status_code == 200:
                    data = json.loads(response.content)
                    for pageid, data in data['query']['pages'].items():
                        if data.get('extract'):
                            doc.meta = data.get('extract')
                            doc.save()
