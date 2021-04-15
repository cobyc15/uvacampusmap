from django.urls import path
from . import views

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.home, name='forum-home'),
    path('newpost/', views.NewPostView.as_view(), name='newpost'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]