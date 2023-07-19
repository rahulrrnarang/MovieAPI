from userAuth.models import Counter
from django.db import transaction

class RequestCounterMiddleware:
    def __init__(self, get_response):
        """Initialize the middleware."""
        self.get_response = get_response

    def __call__(self, request):
        """Call the middleware."""
        with transaction.atomic():
            counter,_ = Counter.objects.get_or_create(
                key='request_count',
                defaults={'value':1}
            )
            counter = Counter.objects.select_for_update().get(key='request_count')
            counter.value += 1
            counter.save()

        response = self.get_response(request)
        return response