from django.views import generic
from django.contrib.auth import views as auth

class LogoutView(auth.LogoutView):
    next_page = 'common:home'
