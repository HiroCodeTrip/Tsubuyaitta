from django.shortcuts import render
from django.http import HttpResponse
from manager.models import Room
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == 'POST':
        room = Room(r_name=request.POST['r_name'], r_auther=request.user)
        room.save()
        return redirect(index)
    
    context = {
        "rooms": Room.objects.all()
    }
    return render(request, 'manager/index.html', context)
