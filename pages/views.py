from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
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
    




class ProductDetailView(DetailView):
    model = Product 
    template_name = 'product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ('name', 'category', 'price', 'stock', 'description')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description', 'stock')
    template_name = 'product_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.store_name != self.request.user:
            raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_del.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.store_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CategoryView(TemplateView):
    model = Product
    template_name = 'categories.html'
    login_urls = 'login'    
