from django.http import JsonResponse
from django.db import models

from indexer.models import DocumentWordIndex, Document


def single_word_search(request):
    search_term = request.GET.get('q', '')

    urls = []
    if search_term:
        urls = DocumentWordIndex.objects.filter(
            word__text__icontains=search_term
        ).values(
            'document_id__url'
        ).annotate(
            total_count=models.Sum('count')
        ).order_by('-total_count')[:5]

    return JsonResponse({'top_hits': list(urls)})


def multi_word_search(request):
    search_terms = request.GET.get('q', '')

    if search_terms:
        query = models.Q()
        for term in search_terms.split(' '):
            query |= models.Q(word__text__icontains=term)
        urls = DocumentWordIndex.objects.filter(
            query
        ).values(
            'document_id__url'
        ).annotate(
            total_count=models.Sum('count')
        ).order_by('-total_count')[:5]

    return JsonResponse({'top_hits': list(urls)})
