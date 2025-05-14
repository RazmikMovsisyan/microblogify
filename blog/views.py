# Standardbibliotheken
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Django Auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Django Messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Django Generic Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

# Lokale Importe
from .models import Post, Profile, Comment
from .forms import CommentForm



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        if not request.user.is_authenticated:
            return redirect('account_login')

        action = request.POST.get('action')
        comment_id = request.POST.get('comment_id')

        if action == "save" and comment_id:
            comment = Comment.objects.get(id=comment_id, post=self.object, author=request.user)
            content = request.POST.get('content')
            if content:
                comment.content = content
                comment.save()
                messages.success(request, "Your comment was updated.")
            return redirect('post_detail', slug=self.object.slug)

        elif action == "delete" and comment_id:
            comment = Comment.objects.get(id=comment_id, post=self.object, author=request.user)
            comment.delete()
            messages.success(request, "Your comment was deleted.")
            return redirect('post_detail', slug=self.object.slug)

        elif action == "edit" and comment_id:
            context['editing_comment_id'] = int(comment_id)
            return self.render_to_response(context)

        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = self.object
                comment.author = request.user
                comment.save()
                messages.success(request, "Your comment was posted.")
                return redirect('post_detail', slug=self.object.slug)

        context['comment_form'] = form
        return self.render_to_response(context)
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post successfully created!")
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        messages.success(self.request, "Your post has been updated.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})

class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    success_message = "Your post has been deleted."

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class UserProfileView(DetailView):
    model = User
    template_name = 'blog/profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object).order_by('-created_on')
        return context
    
@login_required
def profile_view(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-created_on')
    return render(request, 'blog/profile.html', {
        'profile_user': request.user,
        'posts': user_posts,
    })

# User delete function
@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        Post.objects.filter(author=user).delete()
        Profile.objects.filter(user=user).delete()
        user.delete()
        logout(request)
        messages.success(request, "Your profile and all posts have been permanently deleted.")
        return redirect('post_list')  # Oder zur Landing Page
    return redirect('profile')