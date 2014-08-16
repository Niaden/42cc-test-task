from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts
from .forms import ContactsForm
from django.contrib import auth
from django.core.urlresolvers import reverse
# Create your views here.


def show_contacts(request):
    return render(request, 'contacts.html', {
        'contacts': Contacts.objects.get(id="1"),
        'username': auth.get_user(request).username
        })


def edit_data(request):
    username = auth.get_user(request).username
    if username:
        return render(request, 'editdata.html', {
            'form': ContactsForm,
            'username': username
            })
    else:
        return redirect('/auth/login/401/')


def post_contacts(request):
    if request.method == 'POST':
        ob1 = Contacts.objects.get(id="1")
        form = ContactsForm(request.POST, request.FILES, instance=ob1)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacts.views.show_contacts'))
        else:
            return HttpResponse('form is not valid')
    else:
        form = ContactsForm()
    return HttpResponse("error.  it's not a post request")
