from django.contrib import admin
from .models import Meetup
from .models import Event

admin.site.register(Meetup)
admin.site.register(Event)
