from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserProfileView,
    delete_profile,
    profile_view,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    path('profile/', profile_view, name='profile'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('users/<slug:username>/', UserProfileView.as_view(), name='profile'),
]
