import unittest
from django.test import TestCase
from django.core import management
from django.test import Client
from contacts.models import Contacts
from django.contrib.auth.models import User
from contacts.forms import ContactsForm
from django.core.urlresolvers import reverse


class TestContactsViews(TestCase):
    def setUp(self):
        management.call_command('loaddata', 'contacts_damir.json', verbosity=0)

    def test_url2(self):
        resp = self.client.get(reverse('contacts.views.show_contacts'))
        self.failUnlessEqual(resp.status_code, 200)

    def test_view_has_contact_in_context(self):
        resp = self.client.get(reverse('contacts.views.show_contacts'))
        contact = resp.context[-1]['contacts']
        self.failUnlessEqual(contact.contacts_name, u'Damir')
        self.failUnlessEqual(contact.contacts_lastname, u'Ravilov')
        self.failUnlessEqual(contact.contacts_email, u'damir_ne_@mail.ru')
        self.failUnlessEqual(contact.contacts_jabber, u'tuiky@42cc.co')
        self.failUnlessEqual(contact.contacts_skype, u'gavara9')
        self.failUnlessEqual(contact.contacts_othercontacts,
                            u'tel. +38(095)539-68-79')


class AuthTest(TestCase):
    def test_redirect_if_not_authenticated(self):
        self.client = Client()
        User.objects.create_superuser('admin', 'admin@test.com', 'admin')
        response = self.client.get(reverse('contacts.views.edit_data'))
        self.assertEqual(response.status_code, 302)
        #and now test after athenticating
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('contacts.views.edit_data'))
        self.assertEqual(response.status_code, 200)


# class EditContactsViewTest(TestCase):
#     """ test for edit contacts view """
#     def setUp(self):
#         self.client = Client()
#         self.sample_contact = Contacts(
#             contacts_name='Petya',
#             contacts_lastname='Petrov',
#             contacts_birthdate='',
#             contacts_bio='born, lived, loved, died',
#             contacts_email='admin@a.com',
#             contacts_jabber='admin@a.com',
#             contacts_skype='petr1990',
#             contacts_othercontacts='pass'
#         )

#         self.fields = [
#             'contacts_name', 'contacts_lastname', 'contacts_birthdate',
#             'contacts_bio', 'contacts_email', 'contacts_jabber',
#             'contacts_skype', 'contacts_othercontacts'
#         ]
#         # make fake client data
#         self.client_form_data = {}
#         for f in self.fields:
#             self.client_form_data.update({f: getattr(self.sample_contact, f)})

#     def test_form_no_errors(self):
#         """ test case when form is posted with no errors """
#         # first of all login
#         User.objects.create_superuser('admin', 'admin@test.com', 'admin')
#         self.client.login(username='admin', password='admin')

#         # post form
#         response = self.client.post('/editdata/',
#                                     self.client_form_data,
#                                     follow=True)

#         # self.assertEqual(response.contacts_name, 'Petya')

#         # verify saved data
#         contact = Contacts.objects.get(id=1)
#         for f in self.fields:
#             self.assertEqual(getattr(contact, f),
#                              getattr(self.sample_contact, f))
