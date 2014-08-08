from django.shortcuts import render, redirect
from .models import Contacts

# Create your views here.
def show_contacts(request):
	return render(request, 'contacts.html', {'contacts': Contacts.objects.get(id="1")})
