from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from .forms import SignUpForm


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_message = "Your account was created successfully"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('recipe:home')


def profile(request):
    return render(request, 'profile.html', {'user': request.user})
