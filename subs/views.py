from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Subrediti, Thread, Post
from .forms import CreateThreadForm, CreatePostForm

class SubreditisListView(generic.ListView):
    template_name = 'subs/subreditis.html'
    model = Subrediti
    context_object_name = 'subreditis'


class SubreditiDetailView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti


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