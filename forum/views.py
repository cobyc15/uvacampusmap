from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Post

def home(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context={
        'latest_posts': latest_posts
    }
    return render(request, 'forum/index.html', context)

class PostView(generic.ListView):
    model = Post
    template_name = 'forum/posts.html'
    context_object_name = 'all_posts'
    
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/detail.html'

class NewPostView(generic.CreateView):
    model = Post
    fields = ['title','detail']
    template_name = 'forum/newpost.html'