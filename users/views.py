from django.views import generic
from django.contrib import auth
from django.contrib.auth import views, authenticate, get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import UserForm
from .models import User


class LogoutView(views.LogoutView):
    next_page = 'common:home'


class LoginView(views.LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy('common:home')
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:home'))
        return super(LoginView, self).get(request)


class SignupView(generic.FormView):
    form_class = UserForm
    template_name = 'users/signup.html'
    model = get_user_model()
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:home'))
        return super(SignupView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(username=self.object.email, password=form.cleaned_data['password'])
        auth.login(self.request, user)

        return redirect('common:home')


class ProfileView(generic.DetailView):
    template_name = "users/profile.html"
    model = User