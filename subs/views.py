from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Subrediti, Thread, Post, Subscription
from .forms import CreateThreadForm, CreatePostForm
from .helpers import subscribe_or_unsubscribe

class SubreditisListView(generic.ListView):
    template_name = 'subs/subreditis.html'
    model = Subrediti
    context_object_name = 'subreditis'


class SubreditiDetailView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subscription, created = Subscription.objects.get_or_create(user=self.request.user, subrediti=self.object)
        context['subscribed'] = True if subscription.subscribed else False
        return context


class ThreadDetailView(generic.DetailView):
    template_name = 'subs/thread.html'
    model = Thread


class CreateThreadView(generic.CreateView):
    template_name = 'subs/create_thread.html'
    model = Thread
    form_class = CreateThreadForm

    def get_initial(self):
        self.subrediti = self.request.GET.get('sub', None)
        return {
            'subrediti': Subrediti.objects.get(id=self.subrediti),
            'author': self.request.user,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subrediti'] = Subrediti.objects.get(id=self.subrediti)
        return context

    def get_success_url(self):
        subrediti = Subrediti.objects.get(id=self.subrediti)
        return reverse('subs:subrediti', kwargs={'slug': subrediti.slug})


class CreatePostView(generic.CreateView):
    template_name = 'subs/create_post.html'
    model = Post
    form_class = CreatePostForm

    def get_initial(self):
        self.thread = self.request.GET.get('thread', None)
        return {
            'thread': Thread.objects.get(id=self.thread),
            'author': self.request.user,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = Thread.objects.get(id=self.thread)
        return context

    def get_success_url(self):
        thread = Thread.objects.get(id=self.thread)
        return reverse('subs:thread', kwargs={'pk': thread.pk})


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'subs/post_confirm_delete.html'
    success_url = 'home'


class SubscribeView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.subrediti = self.request.GET.get('sub', None)
        subscribe_or_unsubscribe(self.subrediti, self.request.user)
        return self.request.META.get('HTTP_REFERER')