from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

# Create
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'calendar_app/event_form.html', {'form': form})

# Read (List)
def event_list(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'calendar_app/event_list.html', {'events': events})

# Update
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'calendar_app/event_form.html', {'form': form})

# Delete
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'calendar_app/event_confirm_delete.html', {'event': event})