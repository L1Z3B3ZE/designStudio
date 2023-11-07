from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from .forms import RegisterUserForm
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView, DeleteView


# Create your views here.


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logged_out.html'




class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm


class ViewApplications(ListView):
    model = Application
    template_name = 'index.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(status__exact='Выполнено').order_by('-date_create', '-time_create')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_AcceptedForWork'] = Application.objects.filter(status__exact='Принято в работу').count()
        return context


class ApplicationsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'studio/application_list_user.html'
    paginate_by = 10
    context_object_name = 'applications'

    def get_queryset(self):
        status = self.request.GET.get('status')  # получение параметра 'статус' из URL-запроса
        filter = Application.objects.filter(owner=self.request.user).order_by('-date_create', '-time_create')
        if status:
            filter = filter.filter(status=status)
        return filter



class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['application_title', 'description', 'category', 'photo_of_room']
    success_url = reverse_lazy('my-applications')

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('my-applications')
    context_object_name = 'applications'



class ApplicationsAllListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = 'studio/application_list_all.html'
    paginate_by = 10
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.order_by('-date_create', '-time_create')

    def get_queryset(self):
        status = self.request.GET.get('status')  # получение параметра 'статус' из URL-запроса
        filter = Application.objects.order_by('-date_create', '-time_create')
        if status:
            filter = filter.filter(status=status)
        return filter


class ViewCategory(ListView):
    model = Application
    template_name = 'studio/categories_list.html'
    context_object_name = 'categories'
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'studio/categories_list.html', {'categories': categories})

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'studio/category_new.html'
    success_url = reverse_lazy('categories')

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'studio/category_delete.html'
    success_url = reverse_lazy('categories')

    def test_func(self):
        return self.request.user.is_superuser