from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('events1:event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'events1/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('events1:event_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('events1:event_list')
    else:
        form = UserCreationForm()
    return render(request, 'events1/signup.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-date')
    search_query = request.GET.get('search', '')
    if search_query:
        events = events.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    context = {
        'events': events,
        'search_query': search_query,
    }
    return render(request, 'events1/events_list.html', context)

@login_required
def event_det(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'events1/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events1:event_list')
    else:
        form = EventForm()
    return render(request, 'events1/event_form.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            if request.POST.get('clear_image'):
                event.image = None
            elif 'image' in request.FILES:
                event.image = request.FILES['image']
            form.save()
            return redirect('events1:event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events1/event_edit_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return redirect('events1:event_list')

class EventListAPI(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class EventDetailAPI(APIView):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

class EventCreateAPI(APIView):
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class EventUpdateAPI(APIView):
    def put(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class EventDeleteAPI(APIView):
    def delete(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response({'message': 'Event deleted successfully'})