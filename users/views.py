from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone

# Create your views here.

def signup(request):
    return render(request, 'users/signup.html')

def profilesetup(request):
    return render(request, 'users/profilesetup.html')

def profilesetting(request):
    return render(request, 'users/profilesetting.html')


def home(request):
    return render(request, 'users/home.html')


def accountsetting(request):
    return render(request, 'users/accountsetting.html')
