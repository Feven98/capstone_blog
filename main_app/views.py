from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

# class Home(TemplateView):
#     template_name = "home.html"

class Home(ListView):
    model = Blog
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"

