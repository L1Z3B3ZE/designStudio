from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', views.ViewApplications.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('myapplications/', views.ApplicationsByUserListView.as_view(), name='my-applications'),
    path('application/create/', views.ApplicationCreate.as_view(), name='application-create'),
    path('application/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
    path('allapplications/', views.ApplicationsAllListView.as_view(), name='all-applications'),
    path('categories/', views.ViewCategory.as_view(), name='categories'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('application/<int:pk>/change_status/', ChangeRequestStatusView.as_view(), name='application-change-status'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
