from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    forum_post = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date <= now


