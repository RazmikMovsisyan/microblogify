from django.contrib import admin
from django.urls import path, include
from allauth.account import views as allauth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'accounts/login/',
        allauth_views.login,
        name="account_login"
    ),
    path(
        'accounts/signup/',
        allauth_views.signup,
        name="account_signup"
    ),
    path(
        'accounts/logout/',
        allauth_views.logout,
        name="account_logout"
    ),
    path('', include('blog.urls')),
]
