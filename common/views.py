from django.views import generic
from subs.models import Subscription, Subrediti
from .helpers import modify_post_karma

class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['subscriptions'] = Subscription.objects.filter(user=self.request.user)
        context['subreditis'] = Subrediti.objects.all()
        return context


class UpvoteView(generic.RedirectView):
    def dispatch(self, request, *args, **kwargs):
        modify_post_karma()
        return super().dispatch(*args, **kwargs)


class DownvoteView(generic.RedirectView):
    def dispatch(self, request, *args, **kwargs):
        modify_post_karma()
        return super().dispatch(*args, **kwargs)
