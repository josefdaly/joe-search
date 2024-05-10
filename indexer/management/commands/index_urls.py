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
            "https://en.wikipedia.org/wiki/Elon_Musk",
            "https://en.wikipedia.org/wiki/Elephant",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Leonardo_da_Vinci",
            "https://en.wikipedia.org/wiki/Black_hole",
            "https://en.wikipedia.org/wiki/Ancient_Egypt",
            "https://en.wikipedia.org/wiki/The_Beatles",
            "https://en.wikipedia.org/wiki/European_Union",
            "https://en.wikipedia.org/wiki/Climate_change",
            "https://en.wikipedia.org/wiki/Pablo_Picasso",
            "https://en.wikipedia.org/wiki/World_War_II",
            "https://en.wikipedia.org/wiki/Machu_Picchu",
            "https://en.wikipedia.org/wiki/Renaissance",
            "https://en.wikipedia.org/wiki/Stephen_Hawking",
            "https://en.wikipedia.org/wiki/Great_Barrier_Reef",
            "https://en.wikipedia.org/wiki/Vincent_van_Gogh",
            "https://en.wikipedia.org/wiki/Mozart",
            "https://en.wikipedia.org/wiki/Albert_Einstein",
            "https://en.wikipedia.org/wiki/Roman_Empire",
            "https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.",
            "https://en.wikipedia.org/wiki/SpaceX",
            "https://en.wikipedia.org/wiki/Penguins",
            "https://en.wikipedia.org/wiki/Galileo_Galilei",
            "https://en.wikipedia.org/wiki/Napoleon",
            "https://en.wikipedia.org/wiki/Amazon_rainforest",
            "https://en.wikipedia.org/wiki/Marie_Curie",
            "https://en.wikipedia.org/wiki/Global_warming",
            "https://en.wikipedia.org/wiki/Beethoven",
            "https://en.wikipedia.org/wiki/Sigmund_Freud",
            "https://en.wikipedia.org/wiki/Pyramids_of_Giza",
            "https://en.wikipedia.org/wiki/Alexander_the_Great",
            "https://en.wikipedia.org/wiki/NASA",
            "https://en.wikipedia.org/wiki/Socrates",
            "https://en.wikipedia.org/wiki/Hubble_Space_Telescope",
            "https://en.wikipedia.org/wiki/Charles_Darwin",
            "https://en.wikipedia.org/wiki/Mount_Everest",
            "https://en.wikipedia.org/wiki/The_Great_Depression",
            "https://en.wikipedia.org/wiki/Henry_VIII_of_England",
            "https://en.wikipedia.org/wiki/Pandas",
            "https://en.wikipedia.org/wiki/Leon_Trotsky",
            "https://en.wikipedia.org/wiki/Helen_Keller",
            "https://en.wikipedia.org/wiki/Islamic_Golden_Age",
            "https://en.wikipedia.org/wiki/Thomas_Edison",
            "https://en.wikipedia.org/wiki/Great_Wall_of_China",
            "https://en.wikipedia.org/wiki/Johannes_Gutenberg",
            "https://en.wikipedia.org/wiki/Aristotle",
            "https://en.wikipedia.org/wiki/Hawaii",
            "https://en.wikipedia.org/wiki/Amelia_Earhart",
            "https://en.wikipedia.org/wiki/Surrealism",
            "https://en.wikipedia.org/wiki/William_Shakespeare"
        ]
        for url in urls:
            if Document.objects.filter(url=url).exists():
                print('already processed, skipping ' + url)
            else:
                print('processing ' + url)
                index_web_document(url)
