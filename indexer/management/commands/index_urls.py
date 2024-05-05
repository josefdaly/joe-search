from django.core.management.base import BaseCommand, CommandError

from indexer.utilities import index_web_document
from indexer.models import Document


class Command(BaseCommand):

    def handle(self, *args, **options):
        urls = [
            'https://en.wikipedia.org/wiki/Transitional_Presidential_Council',
            'https://en.wikipedia.org/wiki/Haitian_crisis_(2018%E2%80%93present)',
            'https://en.wikipedia.org/wiki/Hinche',
            'https://en.wikipedia.org/wiki/Hispaniola',
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Machine_learning",
            "https://en.wikipedia.org/wiki/Neural_network",
            "https://en.wikipedia.org/wiki/Natural_language_processing",
            "https://en.wikipedia.org/wiki/Data_science",
            "https://en.wikipedia.org/wiki/Quantum_computing",
            "https://en.wikipedia.org/wiki/Blockchain",
            "https://en.wikipedia.org/wiki/Renewable_energy",
            "https://en.wikipedia.org/wiki/Climate_change",
            "https://en.wikipedia.org/wiki/SpaceX",
            "https://en.wikipedia.org/wiki/Tesla,_Inc.",
            "https://en.wikipedia.org/wiki/Leonardo_da_Vinci",
            "https://en.wikipedia.org/wiki/Albert_Einstein",
            "https://en.wikipedia.org/wiki/Marie_Curie",
            "https://en.wikipedia.org/wiki/Nelson_Mandela",
            "https://en.wikipedia.org/wiki/Mahatma_Gandhi",
            "https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.",
            "https://en.wikipedia.org/wiki/Steve_Jobs",
            "https://en.wikipedia.org/wiki/Elon_Musk"
        ]
        for url in urls:
            if Document.objects.filter(url=url).exists():
                print('already processed, skipping ' + url)
            else:
                print('processing ' + url)
                index_web_document(url)
