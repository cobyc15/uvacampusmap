from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def home(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context={
        'latest_posts': latest_posts
    }
    return render(request, 'forum/forumhome.html', context)
