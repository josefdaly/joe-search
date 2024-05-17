from django.http import JsonResponse

from searchengine.celery import call_command_task

def run_command(request):
    COMMANDS = [
        'index_urls',
        'populate_document_meta',
        'populate_page_titles',
    ]

    command_name = request.GET.get('command', None)
    if not command_name:
        return JsonResponse({'error': 'no command specified'})

    if command_name not in COMMANDS:
        return JsonResponse({'error': 'no valid command'})

    call_command_task.delay(command_name)
    return JsonResponse({'success': True})
