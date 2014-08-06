# coding: utf8
from django.contrib import admin
from .models import Contacts

# Register your models here.

#управление отображением Article
class ContactsAdmin(admin.ModelAdmin):
	list_filter = ['contacts_lastname']

admin.site.register(Contacts, ContactsAdmin)
# регистрируем класс, которым можно управлять в админке, и класс, который управляет отображением класса Article