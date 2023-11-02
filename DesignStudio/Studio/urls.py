from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path


urlpatterns = [
    path('', views.ViewRequests.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)