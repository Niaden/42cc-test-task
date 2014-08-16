import unittest
from django.test import TestCase


class TestContextProcessor(TestCase):
    def test_if_my_var_in_context(self):
        response = self.client.get('/admin/')
        self.assertEqual('MY_SETTINGS' in response.context, True)
