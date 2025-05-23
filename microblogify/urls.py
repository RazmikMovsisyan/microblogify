"""
URL configuration for microblogify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from allauth.account import views as allauth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', allauth_views.login, name="account_login"),
    path('accounts/signup/', allauth_views.signup, name="account_signup"),
    path('accounts/logout/', allauth_views.logout, name="account_logout"),
    path('', include('blog.urls')),
    # path('', lambda request: redirect('post_list')),
]
