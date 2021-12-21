from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    class Meta:
        db_table = "Question"

    comment = models.CharField(verbose_name="コメント",max_length=200)

    def __str__(self):
        return self.comment

class Question(models.Model):
    id = models.CharField(max_length=15)
    content = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at =models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.id

