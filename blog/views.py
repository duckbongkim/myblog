from django.shortcuts import render
from .models import Post, Category, Tag, Comment
from django.views.generic import DetailView, TemplateView

class PostDV(TemplateView):
    template_name = 'blog/post_detail.html'
# Create your views here.
