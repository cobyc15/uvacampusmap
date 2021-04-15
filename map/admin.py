from django.contrib import admin
from .models import Measurement
# Register your models here.
admin.site.register(Measurement)

from forum.models import Event
admin.site.register(Event)