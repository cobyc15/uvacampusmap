from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url('',views.home, name="default"),
]
