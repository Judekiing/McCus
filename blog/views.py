from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
from pages.models import Product
from django.http import HttpResponse, HttpResponseRedirect

class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'all_post_list'
    

class BlogDetailView(DetailView):
    model = Post 
    template_name = 'blog_detail.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'updated_at')
    template_name = 'blog_edit.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = ('title', 'body', 'author',)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_del.html'
    success_url = reverse_lazy('blog')



def home_page_view(request):
    return render(request, 'home.html', {
        'all_products_list': Product.objects.all(),
        'all_posts_list': Post.objects.all()
    })
