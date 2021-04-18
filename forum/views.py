from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django import forms
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

'''class NewPostView(generic.CreateView):
    model = Post
    fields = ['title','detail']
    template_name = 'forum/newpost.html'
    def get_success_url(self):
            return render(request, 'polls/submit.html')'''

# def NewPostView(request):
#     if request.method == "POST":
#         ttl=request.POST.get('titleField')
#         det=request.POST.get('deep_text')
#         pub_d = timezone.now()
#
#         if ttl and det:
#             t=Post(title=ttl, detail=det, pub_date = pub_d)
#             t.save()
#
#     return render(request, 'forum/newpost.html')
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

def NewPostView(request):
    if request.method == "POST":
        ttl=request.POST.get('titleField')
        det=request.POST.get('deep_text')
        form = ContactForm(request.POST)  # 2
        pub_d = timezone.now()

        if ttl and det:
            t=Post(title=ttl, detail=det, pub_date = pub_d)
            t.save()
        return main(request)
    else:
        form = ContactForm()

    return render(request, 'forum/newpost.html', {'form': form})
def main(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context={
        'latest_posts': latest_posts
    }
    return render(request, 'forum/index.html', context)
