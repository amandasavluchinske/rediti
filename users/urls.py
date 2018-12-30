from django.urls import path

from .views import LogoutView, LoginView, SignupView, ProfileView

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
