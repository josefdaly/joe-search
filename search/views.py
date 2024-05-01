from django.http import JsonResponse

from indexer.models import DocumentWordIndex, Document


def single_word_search(request):
    query = request.GET.get('q', '')

    urls = []
    if query:
        urls = DocumentWordIndex.objects.filter(word__text__icontains=query,).order_by('-count')
        unique_urls = set(urls.values_list('document__url', flat=True))

    return JsonResponse({'top_hits': list(unique_urls)})
