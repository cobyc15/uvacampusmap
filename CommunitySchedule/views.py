from datetime import timedelta
from datetime import date
import calendar
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import DeleteView
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from .models import *
from .forms import EventForm
from .utils import Calendar
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from geopy.geocoders import Nominatim

def index(request):
    return HttpResponse('hello')

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/google/login'
    model = CommunityEvent
    template_name = 'CommunitySchedule/schedule2.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        schedule = Calendar(d.year, d.month)
        # Call the formatmonth method, which returns our calendar as a table
        html_schedule = schedule.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_schedule)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required
def communityevent(request, event_id=None):
    instance = CommunityEvent()
    if event_id:
        instance = get_object_or_404(CommunityEvent, pk=event_id)
    else:
        instance = CommunityEvent()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and 'save' in request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('CommunitySchedule:CommunitySchedule'))
    # if user presses the delete button
    if request.POST and 'delete' in request.POST:
        if event_id:
            CommunityEvent.objects.filter(pk=event_id).delete()
            return HttpResponseRedirect(reverse('CommunitySchedule:CommunitySchedule'))
    if request.POST and 'location' in request.POST:
        if event_id:
            address = request.POST.get('address')
            try:
                geolocator = Nominatim(user_agent="schedule")
                location = geolocator.geocode(str(address))
                args = {}
                args['lat'] = location.latitude
                args['long'] = location.longitude
                return render(request, 'map/MapTemplate3.html', args)
            except:
                return render(request, 'CommunitySchedule/event2.html', {'form': form})
    return render(request, 'CommunitySchedule/event2.html', {'form': form})
