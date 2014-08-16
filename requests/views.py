from django.shortcuts import render
from .models import Request
from django.contrib import auth

# Create your views here.


def show_requests(request):
    return render(request, 'requests.html', {
        'requests': Request.objects.all()[:10],
        'username': auth.get_user(request).username}
        )
