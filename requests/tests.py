import unittest
from django.test import TestCase
from .models import Request

class RequestsDBTestCase(TestCase):
    def test_requests_db(self):
    	for i in range(10):
    		resp = self.client.get('/showrequests/')	
    	requests = Request.objects.all()
    	counter = 0
    	for request in requests:
    		if request.request_path == "/showrequests/":
    			counter += 1
    	self.assertEqual(counter, 10)