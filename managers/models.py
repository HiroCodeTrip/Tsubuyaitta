from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Room(models. Model):
    r_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    # 最終更新を取得したい
    r_auther =  models.ForeignKey(User, on_delete=models.PROTECT)
