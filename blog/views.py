from django.shortcuts import render
from django.views.generic import ListView
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


# Create your views here.
