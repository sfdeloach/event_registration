from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import Event, Registration
from .forms import EventForm, RegistrationForm
from django.contrib import messages


def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by("date")
    return render(request, "events/event_list.html", {"events": events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "events/event_detail.html", {"event": event})


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, "Event created successfully!")
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request, "events/event_form.html", {"form": form})


@login_required
def event_register(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if Registration.objects.filter(event=event, user=request.user).exists():
                messages.error(request, "You are already registered for this event.")
            else:
                registration = form.save(commit=False)
                registration.event = event
                registration.user = request.user
                registration.save()
                messages.success(request, "Registered successfully!")
            return redirect("event_detail", pk=event.pk)
    else:
        form = RegistrationForm()
    return render(request, "events/event_register.html", {"form": form, "event": event})


@login_required
def dashboard(request):
    events = Event.objects.filter(organizer=request.user)
    registrations = Registration.objects.filter(user=request.user)
    return render(
        request,
        "events/dashboard.html",
        {"events": events, "registrations": registrations},
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
