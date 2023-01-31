from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=150)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.title 
        # return self.title + ' | ' + str(self.writer)

    class Meta:
        ordering = ['title']