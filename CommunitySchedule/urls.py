from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'CommunitySchedule'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='CommunitySchedule'),
    url(r'^event/new/$', views.communityevent, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.communityevent, name='event_edit'),
]

# Hui Wen
# Date made: 24 July 2018
# Web browser Calendar source code
# https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html 
