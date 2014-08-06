from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from .models import Contacts

# Create your views here.

def show_contacts(request):
	return render_to_response('contacts.html', {'contacts': Contacts.objects.get(contacts_name="Damir")})