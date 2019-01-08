from django.urls import path
from subs.views import SubreditisListView, SubreditiDetailView, ThreadDetailView, CreateThreadView, CreatePostView

app_name = 'subs'

urlpatterns = [
    path('subs/', SubreditisListView.as_view(), name='subreditis'),
    path('subs/<slug:slug>/', SubreditiDetailView.as_view(), name='subrediti'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread'),
    path('thread/new/', CreateThreadView.as_view(), name='create_thread'),
    path('post/new/', CreatePostView.as_view(), name='create_post')
]