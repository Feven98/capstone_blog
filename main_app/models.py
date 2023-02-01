from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=150)
    # writer = models.TextField(max_length=300)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    # created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="title")

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