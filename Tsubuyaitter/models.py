from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User
from managers.models import Room

# Create your models here.
class Post(models.Model):
    posted_room = models.ForeignKey(Room, on_delete=CASCADE)
    posted_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    text = models.TextField()
    is_solved = models.BooleanField()
