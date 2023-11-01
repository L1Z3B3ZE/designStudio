from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm
from .models import Applications


# Create your views here.

def index(request):
    Applications_title = Applications.objects.all()
    Applications_description = Applications.description
    Applications_category = Applications.category
    return render(request, 'index.html', context={'Applications_title': Applications_title,
                                                 'Applications_description': Applications_description,
                                                 'Applications_category': Applications_category})


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')