from django.views import generic
from subs.models import Subscription, Subrediti
from .helpers import modify_karma


class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['subscriptions'] = Subscription.objects.filter(user=self.request.user)
        context['subreditis'] = Subrediti.objects.all()
        return context


class VoteView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.target_type = self.request.GET.get('target_type', None)
        self.target_id = self.request.GET.get('target_id', None)
        modify_karma(self.target_type, self.target_id, self.request.user)
        return self.request.META.get('HTTP_REFERER')
