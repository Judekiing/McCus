from django.urls import path 


from .views import home_page_view, BlogPageView


urlpatterns = [
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('', home_page_view, name='blog'),
]

