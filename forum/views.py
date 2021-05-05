from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
import datetime
from django import forms
from .models import Post, Comment
from schedule.models import Event
from CommunitySchedule.models import CommunityEvent
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    latest_posts = Post.objects.order_by('-pub_date')[:10]
    latest_events = CommunityEvent.objects.filter(start_time__gte=datetime.datetime.now())[:10]
    context={
        'latest_posts': latest_posts,
        'latest_events': latest_events
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

    #comments = post.comments


#@login_required(provi)
class ProfileView(generic.ListView): 
    model = Post
    context_object_name = 'profile_list'
    template_name = 'forum/MyProfile.html'

    # reference: https://stackoverflow.com/questions/43847173/cannot-import-models-from-another-app-in-django
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        qs = []
        qs2 = []
        if self.request.user.is_authenticated:
            qs = self.model.objects.filter(author=self.request.user)
            qs2 = Event.objects.filter(author=self.request.user, start_time__gte=datetime.datetime.now())[:5]
        context['my_posts'] = qs
        context['events'] = qs2    #Event.objects.all()

        return context

    """ def get_queryset(self):
        qs = []
        if self.request.user.is_authenticated:
            qs = self.model.objects.filter(author=self.request.user)
        else:
            qs = []
        #list = Post.objects.filter(author=request.user)
        #return Post.objects.order_by('-pub_date')
        return qs  """

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('forum:forum-home')

'''class NewPostView(generic.CreateView):
    model = Post
    fields = ['title','detail']
    template_name = 'forum/newpost.html'
    def get_success_url(self):
            return render(request, 'polls/submit.html')'''

""" # def NewPostView(request):
#     if request.method == "POST":
#         ttl=request.POST.get('titleField')
#         det=request.POST.get('deep_text')
#         pub_d = timezone.now()
#
#         if ttl and det:
#             t=Post(title=ttl, detail=det, pub_date = pub_d)
#             t.save()
#
#     return render(request, 'forum/newpost.html') """

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

@login_required
def NewPostView(request):
    if request.method == "POST":
        ttl=request.POST.get('titleField')
        det=request.POST.get('deep_text')
        form = ContactForm(request.POST)  # 2
        pub_d = timezone.now()
        aut = request.user

        if ttl and det:
            t=Post(title=ttl, detail=det, pub_date = pub_d, author=aut)
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
