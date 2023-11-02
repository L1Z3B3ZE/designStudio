from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import RegisterUserForm
from .models import Application
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView


# Create your views here.


class BBLoginView(LoginView):
   template_name = 'registration/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'registration/logged_out.html'

class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class ViewApplications(ListView):
   model = Application
   template_name = 'index.html'
   context_object_name = 'applications'

   def get_queryset(self):
       return Application.objects.filter(status__exact='Выполнено').order_by('-date_create')[:4]



   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['num_AcceptedForWork'] = Application.objects.filter(status__exact='Принято в работу').count()
       return context


