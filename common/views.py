from django.views import generic
from subs.models import Subscription, Subrediti

class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['subscriptions'] = Subscription.objects.filter(user=self.request.user)
        context['subreditis'] = Subrediti.objects.all()
        return context
