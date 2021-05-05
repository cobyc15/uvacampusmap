from django.db import models
from django.urls import reverse

class CommunityEvent(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default="1826 University Ave, Charlottesville")
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    @property
    def get_html_url(self):
        url = reverse('CommunitySchedule:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
# Hui Wen
# Date made: 24 July 2018
# Web browser Calendar source code
# https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html 
