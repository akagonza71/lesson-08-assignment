from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post, Category

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'