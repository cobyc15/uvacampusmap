from django.conf.urls import url
from . import views

app_name = 'schedule'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^schedule/$', views.CalendarView.as_view(), name='schedule')
]