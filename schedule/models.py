from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField(max_length=200, default="85 Engineer's Way, Charlottesville, VA 22903")
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    @property
    def get_html_url(self):
        url = reverse('schedule:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'