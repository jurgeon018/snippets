from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
