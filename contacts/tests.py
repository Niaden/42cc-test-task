import unittest
from django.test import TestCase
from django.core import management


class TestContactsViews(TestCase):
    def setUp(self):
        management.call_command('loaddata', 'contacts_damir.json', verbosity=0)   

    def test_url1(self):
        resp = self.client.get('/admin/')
        self.assertEqual(resp.status_code, 300)

    def test_url2(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 300)

    def test_url3(self):
        resp = self.client.get('/showcontacts/')
        self.assertEqual(resp.status_code, 300)

    def test_default_view_has_contact_in_context(self):
        resp = self.client.get('/')
        contact = resp.context[-1]['contacts']
        self.assertEqual(contact.contacts_name, u'Petya')
