import unittest
from django.test import TestCase
from .models import Request
from django.core.urlresolvers import reverse


class RequestsDBTestCase(TestCase):
    def test_requests_db(self):
        for i in range(10):
            resp = self.client.get(reverse('requests.views.show_requests'))
        requests = Request.objects.all()
        counter = 0
        for request in requests:
            if request.request_path == "/showrequests/":
                counter += 1
        self.assertEqual(counter, 10)
