from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    tweets = models.ManyToManyField('Post', blank=True, related_name="post_user") 

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length = 20)
    body = models.CharField(max_length= 150)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.body}; likes: {self.likes}"
