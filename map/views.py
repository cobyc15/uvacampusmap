# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def MapTemplate(request):
     # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYmRuNGVmIiwiYSI6ImNrbXVhNnUybzBoY3kyd28ycHRtYXNiNWwifQ.YzHAdcSZGaN1qP37urA7ew'
    return render(request, 'map/MapTemplate.html', {'mapbox_access_token ': mapbox_access_token })

@login_required
def MapTemplate2(request):
     # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYmRuNGVmIiwiYSI6ImNrbXVhNnUybzBoY3kyd28ycHRtYXNiNWwifQ.YzHAdcSZGaN1qP37urA7ew'
    return render(request, 'map/MapTemplate2.html', {'mapbox_access_token ': mapbox_access_token })

@login_required
def MapTemplate3(request):
     # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYmRuNGVmIiwiYSI6ImNrbXVhNnUybzBoY3kyd28ycHRtYXNiNWwifQ.YzHAdcSZGaN1qP37urA7ew'
    return render(request, 'map/MapTemplate3.html', {'mapbox_access_token ': mapbox_access_token })
