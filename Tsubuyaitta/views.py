from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone

# Create your views here.
def appexplanation(request):
    return render(request,'Tsubuyaitta/appex.html')

def termsofservice(request):
    return render(request,'Tsubuyaitta/termsofservice.html')

def tutorial(request):
    return render(request,'Tsubuyaitta/tutorial.html')

def maketheroom(request):
    return render(request,'Tsubuyaitta/maketheroom.html')

def jointheroom(request):
    return render(request,'Tsubuyaitta/jointheroom.html')

def directmessage(request):
    return render(request,'Tsubuyaitta/directmessage.html')