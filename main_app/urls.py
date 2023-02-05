from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name="blog_detail"),
    path('blog/new', views.BlogCreate.as_view(), name= "blog_create"),
    path('blog/<int:pk>/update', views.BlogUpdate.as_view(), name= "blog_update"),
    path('blog/<int:pk>/delete', views.BlogDelete.as_view(), name= "blog_delete"),
    path('blog/<int:pk>/comments/new', views.CommentCreate.as_view(), name="comment_create"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
    path('blog/<int:blog_id>/add_photo/', views.NewPhoto.as_view(), name="add_photo"),
    path('blog/<int:blog_id>/update_photo', views.UpdatePhoto.as_view(), name="update_photo"),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('profile_edit/', views.EditProfile.as_view(), name="profile_edit"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name = "registration/password_change.html")),
]