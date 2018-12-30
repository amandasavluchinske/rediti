from django.contrib import admin
from .models import Subrediti, Thread, Post, Subscription

admin.site.register(Subrediti)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Subscription)
