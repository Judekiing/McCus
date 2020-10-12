from django.urls import path 


from .views import (
    home_page_view,
     AboutPageView,
     ProductDetailView,
     ProductCreateView,
     ProductDeleteView,
     ProductUpdateView,
     CategoryView,
)



urlpatterns = [
  
    path('about/', AboutPageView.as_view(), name='about'),
    path('cate/', CategoryView.as_view(), name='category'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_del'),
    path('product/new/', ProductCreateView.as_view(), name='product_new'),
    path('/', home_page_view, name='home'),
]

