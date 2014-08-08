import unittest
from django.test import TestCase
from django.core import management


class TestContactsViews(TestCase):
    def setUp(self):
        management.call_command('loaddata', 'contacts_damir.json', verbosity=0)   

    def test_url1(self):
        resp = self.client.get('/admin/')
        self.assertEqual(resp.status_code, 200)

    def test_url2(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url3(self):
        resp = self.client.get('/showcontacts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_has_contact_in_context(self):
        resp = self.client.get('/')
        contact = resp.context[-1]['contacts']
        self.failUnlessEqual(contact.contacts_name, u'Damir')
        self.failUnlessEqual(contact.contacts_lastname, u'Ravilov')
        self.failUnlessEqual(contact.contacts_email, u'damir_ne_@mail.ru')
        self.failUnlessEqual(contact.contacts_jabber, u'tuiky@42cc.co')
        self.failUnlessEqual(contact.contacts_skype, u'gavara9')
        self.failUnlessEqual(contact.contacts_othercontacts, u'tel. +38(095)539-68-79')
