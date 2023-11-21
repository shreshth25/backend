from django.contrib import admin
from .models import User, Post, Reel
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Reel)