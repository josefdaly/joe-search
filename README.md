Extremely rudimentary search engine implemented in Django.

So far:
websites can be indexed via the command `python manage.py index_urls`
You can manually add sites to index there.

The indexer creates a very basic reverse index using 3 data models, Word, Document and DocumentWordIndex. The amount of times a word is present in a specific document counted in the DocumentWordIndex model.
