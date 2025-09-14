from django import forms
from .models import Event, Registration
from django.utils import timezone


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "date"]
        widgets = {"date": forms.DateTimeInput(attrs={"type": "datetime-local"})}

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.now():
            raise forms.ValidationError("The event date cannot be in the past.")
        return date


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []  # No fields needed; user and event set in view
