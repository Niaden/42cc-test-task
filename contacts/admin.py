# coding: utf8
from django.contrib import admin
from .models import Contacts

# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_filter = ['contacts_lastname']

admin.site.register(Contacts, ContactsAdmin)
