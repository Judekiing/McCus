from django.urls import path 


from .views import (
    # home_page_view, 
    BlogPageView,
    BlogUpdateView,
    BlogDetailView,
    BlogCreateView,
    BlogDeleteView,
)           


urlpatterns = [ 
   
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_del'),
    path('new/', BlogCreateView.as_view(), name='blog_new'),
    path('', BlogPageView.as_view(), name='blog'),
    # path('blog/', home_page_view, name='home'),
]

