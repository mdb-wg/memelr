from django.contrib import admin

# Register your models here.
from .models import Post, Response

admin.site.register(Post)
admin.site.register(Response)