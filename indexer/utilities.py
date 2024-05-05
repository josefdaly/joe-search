import requests, re
from bs4 import BeautifulSoup

from indexer.constants import STOP_WORDS
from indexer.models import DocumentWordIndex, Word, Document


def add_to_index(text, url):
    document, _ = Document.objects.get_or_create(url=url)
    word, _ = Word.objects.get_or_create(text=text)
    index, _ = DocumentWordIndex.objects.get_or_create(document=document, word=word)
    index.count += 1
    index.save()


def normalize_encoding(text):
    if isinstance(text, bytes):
        normalized_text = text.decode('utf-8', 'ignore')
    else:
        normalized_text = text.encode('utf-8', 'ignore').decode('utf-8')
    return normalized_text


def clean_text(text):
    # Remove punctuation using regular expression
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    cleaned_text = cleaned_text.strip().lower()
    return cleaned_text


def index_web_document(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = BeautifulSoup(response.content).get_text()
        normalized_url = normalize_encoding(url)
        for word in text.split(' '):
            normalized_word = normalize_encoding(clean_text(word))
            if normalized_word in STOP_WORDS:
                continue
            add_to_index(
                normalized_word,
                normalized_url,
            )
