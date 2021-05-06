"""
REFERENCES
*  Title: Writing your first Django app
*  Author: Django Software Foundation
*  Date: 5/4/2021
*  Code version: 3.2
*  URL: https://docs.djangoproject.com/en/3.2/intro/tutorial03/
"""
from django.urls import path
from django.conf.urls import url, include
from . import views
from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.home, name='forum-home'),
    path('newpost/', views.NewPostView, name='newpost'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
