from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Blog
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
                return reverse('blog_detail', kwargs={'pk':self.object.pk})
