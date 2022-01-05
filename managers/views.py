from django.shortcuts import render
from django.http import HttpResponse
from managers.models import Room
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == 'POST':
        room = Room(r_name=request.POST['r_name'], r_auther=request.user)
        room.save()
        return redirect('home')

    return render(request, 'managers/index.html')
