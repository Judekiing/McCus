from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render 
from .models import Product
from blog.models import Post 


def index(request):
    products = Product.objects.all()
    return render (request, 'base.html', {'products': products})


class HomePageView(ListView):

    model = Product
    
    template_name = 'home.html'

    context_object_name = 'all_products_list'
    
def home_page_view(request):
    return render(request, 'home.html', {
        'all_products_list': Product.objects.all(),
        'all_posts_list': Post.objects.all()
    })


class AboutPageView(TemplateView):

    template_name = 'about.html'


class BlogPageView(ListView):

    model = Post

    template_name = 'blog.html'

    context_object_name =  'all_post_list'
    

