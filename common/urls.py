from django.urls import path

from common.views import HomeView

app_name = 'common'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]