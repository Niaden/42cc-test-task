from .models import Request
from django.utils import timezone


class WebRequestMiddleware(object):
    def process_request(self, request):
        req_path = request.get_full_path()
        req_method = request.method
        req_datetime = timezone.now()
        request_ob = Request(
            request_date=req_datetime,
            request_method=req_method,
            request_path=req_path
            )
        request_ob.save()
        return None
