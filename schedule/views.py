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
from geopy.geocoders import GoogleV3

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'schedule/schedule.html'
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

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and 'save' in request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('schedule:schedule'))
    # if user presses the delete button
    if request.POST and 'delete' in request.POST:
        if event_id:
            Event.objects.filter(pk=event_id).delete()
            return HttpResponseRedirect(reverse('schedule:schedule'))
    if request.POST and 'view' in request.POST:
        address = request.POST.get('address')
        str(address)
        print(address)
        geolocator = GoogleV3(api_key="AIzaSyCXn97mV9a3N8YvGK5LJ7VrDN-Z_tInXus")
        geolocator.geocode(address, timeout=10, exactly_one=False)
        print('success')
        return render(request, 'map/MapTemplate3.html', {'form': form})
    return render(request, 'schedule/event.html', {'form': form})
