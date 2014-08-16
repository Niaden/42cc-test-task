# coding: utf-8
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib import auth

# Create your views here.


def auth_login(request, auth_error=None):
    args = {}
    if auth_error == "401":
        args['auth_error'] = "You are unauthorised! Pls login. "
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['auth_error'] = "User is not found"
            return render(request, 'auth_login.html', args)
    else:
        return render(request, 'auth_login.html', args)


def auth_logout(request):
    auth.logout(request)
    return redirect('/')
