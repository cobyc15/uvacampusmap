
"""CampusMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from forum import views

urlpatterns = [
    path('',login_required(TemplateView.as_view(template_name= "map/index.html"))),
    path('', login_required(include('django.contrib.auth.urls'))),
    path('admin/', admin.site.urls),
    path('accounts/', login_required(include('allauth.urls'))),
    path('map/', login_required(include('map.urls'))),
    path('forum/', login_required(include('forum.urls'))),
    path('myprofile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('myprofile/', login_required(include('schedule.urls'))),
    #path('accounts/logout', include('allauth.urls')),
]
