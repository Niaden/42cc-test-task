from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Request

# Create your views here.
def show_requests(request):
 	return render(request, 'requests.html', {'requests': Request.objects.all()[:10]})