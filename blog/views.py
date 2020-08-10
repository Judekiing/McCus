from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from pages.models import Product
from django.http import HttpResponse

class BlogPageView(ListView):

    model = Post

    template_name = 'home.html'

    context_object_name = 'all_post_list'
    

def home_page_view(request):
    return render(request, 'home.html', {
        'all_products_list': Product.objects.all(),
        'all_posts_list': Post.objects.all()
    })

class BlogDetailView(DetailView):

    model = Post 

    template_name = 'single.html'
# Create your views here.
