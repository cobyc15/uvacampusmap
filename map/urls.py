from django.conf.urls import url
from . import views

urlpatterns = [
    url('template/', views.MapTemplate, name="default"),
    url('template2/', views.MapTemplate2, name="default"),
]
