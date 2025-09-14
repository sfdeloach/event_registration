from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Event, Registration
from .forms import EventForm
import datetime


class EventSystemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", password="testpass123"
        )
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date=timezone.now() + datetime.timedelta(days=1),
            organizer=self.user,
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "Test Event")
        self.assertEqual(self.event.organizer, self.user)

    def test_event_form_valid(self):
        form_data = {
            "title": "New Event",
            "description": "Description",
            "date": timezone.now() + datetime.timedelta(days=2),
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_event_form_invalid_past_date(self):
        form_data = {
            "title": "Invalid Event",
            "description": "Description",
            "date": timezone.now() - datetime.timedelta(days=1),
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors)

    def test_registration_unique(self):
        Registration.objects.create(event=self.event, user=self.user)
        duplicate = Registration(event=self.event, user=self.user)
        with self.assertRaises(Exception):
            duplicate.save()

    def test_event_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")

    def test_event_create_view_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get("/event/new/")
        self.assertEqual(response.status_code, 200)

    def test_event_create_view_unauthenticated(self):
        response = self.client.get("/event/new/")
        self.assertNotEqual(response.status_code, 200)  # Redirects to login

    def test_event_register_authorization(self):
        self.client.login(username="otheruser", password="testpass123")
        response = self.client.post(f"/event/{self.event.pk}/register/")
        registration = Registration.objects.filter(
            event=self.event, user=self.other_user
        )
        self.assertTrue(registration.exists())
