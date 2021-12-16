from typing import Text
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404
from manager.models import Room
from Tsubuyaitta.models import Post
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request, 'Tsubuyaitta/index.html')

def room(request, room_id):
    if request.method == 'POST':
        post = Post(
            text=request.POST['text'],
            posted_room=room_id,
            owner=request.user
        )
        post.save()
        return redirect(request, room_id)

    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    context = {
        'room': room
    }
    return render(request, 'Tsubuyaitta/room.html',context)
