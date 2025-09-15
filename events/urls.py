from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Root URL: List upcoming events
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # Event details
    path('event/new/', views.event_create, name='event_create'),  # Create new event
    path('event/<int:pk>/register/', views.event_register, name='event_register'),  # Register for an event
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard
    path('accounts/signup/', views.signup, name='signup'),  # Custom signup view
]
