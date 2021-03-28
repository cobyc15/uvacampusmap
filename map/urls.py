from django.conf.urls import url
from . import views

urlpatterns = [
    url('template/', views.MapTemplate, name="default"),
]
