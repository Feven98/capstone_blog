from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Blog, Comment, Photo
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import uuid
import boto3
import os
from .forms import SignUpForm
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
    
    def get_context_data(self, **kwargs):
            context = super(BlogDetail, self).get_context_data(**kwargs)
            button = get_object_or_404(Blog, id=self.kwargs['pk'])
            total_likes = button.total_likes
            liked = False
            if button.likes.filter(id=self.request.user.id):
                liked = True

            context["total_likes"]= total_likes
            context["liked"] = liked
            return context

class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'content', 'spoiler']
    template_name = "blog_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.writer = self.request.user
        return super(BlogCreate, self).form_valid(form)

    def get_success_url(self):
                return reverse('home')
                

#  Update post blog
class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'writer', 'content', 'spoiler']
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
class CommentCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        content = request.POST.get("content")
        blog = Blog.objects.get(pk=pk)
        Comment.objects.create(name=name, content=content, blog=blog)
        return redirect('blog_detail', pk=pk)
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = SignUpForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


def add_photo(request, blog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
    try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, blog_id=blog_id)
    except:
            print('An error occurred uploading file to S3')
            # return redirect('blog_detail', blog_id=blog_id)  
            # return reverse('home')

class NewPhoto(View):
    def get(self,request, blog_id):
        # print(blog)
        blog = Blog.objects.get(pk=blog_id)
        print(blog.pk)
        return render(request, "add_photo.html", {"blog" : blog})
    def post(self, request, blog_id):
        photo_file = request.FILES.get('photo-file', None)
        print(photo_file)
        if photo_file:
            s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, blog_id=blog_id)
        except:
            print('An error occurred uploading file to S3')
            return redirect("home")
        return redirect(f"/blog/{blog_id}")
    
class UpdatePhoto(View):
    def get(self,request, blog_id):
        # print(blog)
        blog = Blog.objects.get(pk=blog_id)
        print(blog.pk)
        return render(request, "update_photo.html", {"blog" : blog})
    def post(self, request, blog_id):
        photo_file = request.FILES.get('photo-file', None)
        print(photo_file)
        if photo_file:
            s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, blog_id=blog_id)
        except:
            print('An error occurred uploading file to S3')
            return redirect("home")
        return redirect(f"/blog/{blog_id}/update")
    
def LikeView(request, pk):
     blog=  get_object_or_404(Blog, id=request.POST.get('blog_id'))
     liked = False
     if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
     else:
        blog.likes.add(request.user)
        liked= True
     return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


