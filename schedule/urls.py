from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'schedule'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^schedule/$', views.CalendarView.as_view(), name='schedule'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
# Hui Wen
# Date made: 24 July 2018
# Web browser Calendar source code
# https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
