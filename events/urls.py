from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/<int:pk>/", views.event_detail, name="event_detail"),
    path("event/new/", views.event_create, name="event_create"),
    path("event/<int:pk>/register/", views.event_register, name="event_register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/signup/", views.signup, name="signup"),
]
