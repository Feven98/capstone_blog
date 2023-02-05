from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=150)
    # writer = models.TextField(max_length=300)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = models.TextField(max_length=300)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="title")
    likes = models.ManyToManyField(User, related_name='blog_posts')
    spoiler = models.CharField(max_length=150, default='')
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title 
        # return self.title + ' | ' + str(self.writer)

    class Meta:
        ordering = ['title']

#  Model for comment section
class Comment(models.Model):

    name = models.CharField(max_length=100)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for blog_id: {self.blog_id} @{self.url}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
