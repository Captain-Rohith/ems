from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    capacity = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title