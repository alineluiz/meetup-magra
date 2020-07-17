from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date


class Meetup(models.Model):
    id_meetup = models.AutoField(primary_key=True, blank=False)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to = 'meetups/', null = True, blank = False)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Event(models.Model):
    id_meetup = models.ForeignKey(Meetup, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    event_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title       

@property
def is_past_due(self):
    return timezone.now() > self.event_date

    