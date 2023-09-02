"""eshop URL Configuration

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
from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views

from account.auth_views import RegisterAPI, LoginAPI
from account.views import log_in, register, log_out, verification
from product.views import home, search
from .api import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='api_register'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='api_logoutall'),
    path('', home, name='home'),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('login/', log_in, name='login'),
    path('verification/', verification, name='verification'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
