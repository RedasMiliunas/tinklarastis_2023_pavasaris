from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post, Comment

# Create your views here.
# class PostListView(generic.ListView):
#     model = Post
#     template_name = 'posts.html'
#     context_object_name = 'posts'
#     paginate_by = 10