from django.contrib import admin
from .models import VotePost, VoteThread

admin.site.register(VotePost)
admin.site.register(VoteThread)