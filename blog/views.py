from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView


class AllBlog(ListView):
    template_name = 'blog/all_blogs.html'
    model = Blog
    context_object_name = 'blogs'


class OneBlog(DetailView):
    template_name = 'blog/one_blog.html'
    model = Blog




