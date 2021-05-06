"""
REFERENCES
*  Title: Writing your first Django app
*  Author: Django Software Foundation
*  Date: 5/4/2021
*  Code version: 3.2
*  URL: https://docs.djangoproject.com/en/3.2/intro/tutorial03/

"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now() - datetime.timedelta(days=1)
        return self.pub_date <= now

# reference: https://stackoverflow.com/questions/60497516/django-add-comment-section-on-posts-feed
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
