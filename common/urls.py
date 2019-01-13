from django.urls import path

from common.views import HomeView, VoteView

app_name = 'common'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vote', VoteView.as_view(), name='vote'),
]