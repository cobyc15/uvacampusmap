from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url('', views.MapTemplate, name="default"),
    url('template2/', views.MapTemplate2, name="default"),
    url('template3/', views.MapTemplate3, name="default"),
]
