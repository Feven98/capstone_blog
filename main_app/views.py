from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Blog, Comment
# Create your views here.

# class Home(TemplateView):
#     template_name = "home.html"

class Home(ListView): # Blog shown page
    model = Blog
    template_name = "home.html"


class About(TemplateView):  # not sure what to include but needed
    template_name = "about.html"

class BlogDetail(DetailView):  # Blog detail page
    model = Blog
    template_name = "blog_detail.html"

class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'writer', 'content']
    template_name = "blog_create.html"

    def get_success_url(self):
                return reverse('home')

#  Update post blog
class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'writer', 'content']
    template_name = "blog_update.html"

    def get_success_url(self):
                return reverse('blog_detail', kwargs={'pk':self.object.pk})

#  Delete post blog
class BlogDelete(DeleteView):
    model = Blog
    template_name = "blog_delete.html"
   
    def get_success_url(self):
                return reverse('home')

# Comment create
class CommentCreate(CreateView):

    def post(self, request, pk):
        name = request.POST.get("name")
        content = request.POST.get("content")
        blog = Blog.objects.get(pk=pk)
        Comment.objects.create(name=name, content=content)
        return redirect('blog_detail', pk=pk)
    