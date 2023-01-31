from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name="blog_detail"),
    path('blog/new', views.BlogCreate.as_view(), name= "blog_create"),
]