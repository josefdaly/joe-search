from django.core.management.base import BaseCommand, CommandError

from indexer.utilities import index_web_document


class Command(BaseCommand):

    def handle(self, *args, **options):
        urls = [
            'https://en.wikipedia.org/wiki/Transitional_Presidential_Council',
            'https://en.wikipedia.org/wiki/Haitian_crisis_(2018%E2%80%93present)',
            'https://en.wikipedia.org/wiki/Hinche',
            'https://en.wikipedia.org/wiki/Hispaniola'
        ]
        for url in urls:
            print('processing ' + url)
            index_web_document(url)
