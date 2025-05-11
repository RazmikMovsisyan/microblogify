from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import path
from .models import Post

# shows all posts as list
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# shows single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# create new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

# edit existing post
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

# delete post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')