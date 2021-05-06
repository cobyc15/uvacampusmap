"""
REFERENCES
*  Title: Writing your first Django app
*  Author: Django Software Foundation
*  Date: 5/4/2021
*  Code version: 3.2
*  URL: https://docs.djangoproject.com/en/3.2/intro/tutorial03/
"""
from django.test import TestCase
from django.utils import timezone

import datetime

from .models import Post

class PostModelTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        # was_published_recently() returns False for posts with pub_date in future
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)


