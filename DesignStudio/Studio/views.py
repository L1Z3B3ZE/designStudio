from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView
from .forms import RegisterUserForm
#from .models import Application
from .models import Application


# Create your views here.


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class ViewRequests(ListView):
   model = Application
   template_name = 'index.html'
   context_object_name = 'applications'

