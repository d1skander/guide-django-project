from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegForm, AuthForm


def main_page(request):
    return render(request, 'main.html')


def sight_page(request):
    return render(request, 'sight.html')


def reg_page(request):
    reg_form = RegForm(request.POST)
    if reg_form.is_valid():
        username = reg_form.cleaned_data["username"]
        email = reg_form.cleaned_data["email"]
        password = reg_form.cleaned_data["password"]
        user = User.objects.create_user(username, email, password)
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, user)
            return redirect("main")
        else:
            return HttpResponse("invalid login")
    return render(request, 'reg.html', {"form": reg_form})


def auth_page(request):
    auth_form = AuthForm(request.POST)
    if auth_form.is_valid():
        username = auth_form.cleaned_data["username"]
        password = auth_form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("invalid login")
    else:
        return render(request, 'auth.html', {"form": auth_form})


def info_page(request):
    return render(request, 'info.html')


def logout_func(request):
    logout(request)
    redirect("main")