from typing import Text
from django.contrib.auth.models import User
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import  Http404
from managers.models import Room
from Tsubuyaitter.models import Post
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context = {
        "rooms": Room.objects.all()
    }
    return render(request, 'tsubuyaitter/index.html', context)

def room(request, room_id):
    if request.method == 'POST':
        room = Room.objects.get(pk=room_id)
        post = Post(
            text=request.POST['text'],
            posted_room=room,
            owner=request.user,
            is_solved=False,
        )
        post.save()
        return redirect('room', room_id=room_id)

    try:
        posts = Post.objects.filter(posted_room=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    context = {
        'posts': posts,
        'room_id': room_id,
    }
    return render(request, 'tsubuyaitter/room.html',context)

def home(request):
    contents = {
        'usernames':User.objects.order_by('-id'),
        'rooms':Room.objects.order_by('-created_at')
    }
    return render(request, 'tsubuyaitter/home.html', contents)