from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event


class EventList(ListView):

    model = Event
    context_object_name = 'events'
    template_name = 'calender/eventslist.html'


class EventDetail(DetailView):

    model = Event
    context_object_name = 'event'
    template_name = 'calender/eventsdetail.html'
