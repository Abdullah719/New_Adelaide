from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     email = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(blank=True,null=True,upload_to='media/')
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    user  = models.OneToOneField(User)
    pic = models.ImageField(blank=True,upload_to='/media/')

    def __str__(self):
        return self.user.username