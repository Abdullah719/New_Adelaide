from django.contrib import admin
from django.contrib.auth.models import User
from first_app.models import UserInfo,Post

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Post)