from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
from pages.models import Product
from django.http import HttpResponse, HttpResponseRedirect

class BlogPageView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'all_post_list'
    login_url = 'login'

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post 
    template_name = 'blog_detail.html'
    login_url = 'login'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'blog_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog_del.html'
    success_url = reverse_lazy('blog')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)








def home_page_view(request):
    return render(request, 'home.html', {
        'all_products_list': Product.objects.all(),
        'all_posts_list': Post.objects.all()
    })
