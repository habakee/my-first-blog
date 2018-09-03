import uuid
from django.db import models
from django.utils import timezone

class Post(models.Model):


    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.status == self.STATUS_PUBLIC
        self.save()