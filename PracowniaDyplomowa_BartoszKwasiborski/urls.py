"""PracowniaDyplomowa_BartoszKwasiborski URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
from PracowniaDyplomowa_BartoszKwasiborski import settings
from app.views import register_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main_page.html'), name='main_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
                      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                      path("register/", register_request, name='register'),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


