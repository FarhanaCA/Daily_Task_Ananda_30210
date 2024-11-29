from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event

from django.shortcuts import redirect
from .forms import EventForm

from django.shortcuts import get_object_or_404

from rest_framework import generics
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

@login_required
def event_list(request):
    category = request.GET.get('category', None)
    if category:
        events = Event.objects.filter(category=category)
    else:
        events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.created_by != request.user:
        return redirect('event-list')  # Restrict access to only the creator

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.created_by != request.user:
        return redirect('event-list')

    if request.method == 'POST':
        event.delete()
        return redirect('event-list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve, Update, Delete
class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

