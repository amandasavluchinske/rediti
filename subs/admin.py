from django.contrib import admin
from .models import Subrediti, Thread, Post, Subscription

class SubreditiAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'creator']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Subrediti, SubreditiAdmin)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Subscription)
