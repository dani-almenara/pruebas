from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Event, CountryCodes, TypeEvent
from rest_framework.filters import SearchFilter


class EventList(generic.ListView):
    #template_name = 'events/index.html'
    context_object_name = 'event_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context = super(EventList, self).get_context_data(**kwargs)
        context['place_id'] = self.kwargs.get('place_id')
        print(context)
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by('-init_date')[:5]


class EventDetail(generic.DetailView):
    model = Event
    

