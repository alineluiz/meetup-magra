from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Meetup
from .models import Event

def meetup_list(request):
    meetups = Meetup.objects.select_related().all()
    return render(request, 'meetup/meetup_list.html', {'meetups': meetups})

def meetup_detail(request, pk):
    meetup = get_object_or_404(Meetup, pk=pk)
    events = Event.objects.filter(id_meetup=pk).order_by('-event_date')
    return render(request, 'meetup/meetup_detail.html', {'meetup': meetup, 'events': events})