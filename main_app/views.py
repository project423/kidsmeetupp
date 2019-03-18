from django.shortcuts import render

from django.http import HttpResponse

from .models import Event, Child

from django.views.generic import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    success_url = '/events/'

class EventUpdate(UpdateView):
    model=Event
    fields = '__all__'

class EventDelete(DeleteView):
    model=Event
    success_url = '/events/'





def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    childs = Child.objects.all()
    return render(request, 'profile/profile.html',{'childs':childs})

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events':events})

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', {'event': event})

