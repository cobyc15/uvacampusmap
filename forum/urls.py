from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.home, name='forum-home'),
    path('newpost/', views.NewPostView, name='newpost'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]
