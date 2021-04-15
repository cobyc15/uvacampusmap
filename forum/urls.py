from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='forum-home'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]