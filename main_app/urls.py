from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name="blog_detail"),
    path('blog/new', views.BlogCreate.as_view(), name= "blog_create"),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name= "blog_update"),
    path('blog/<int:pk>/delete', views.BlogDelete.as_view(), name= "blog_delete"),
    path('blog/<int:pk>/comments/new', views.CommentCreate.as_view(), name="comment_create"),
    path('accounts/', include('django.contrib.auth.urls')),
]