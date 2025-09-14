# Project Setup

1. Create directory: `mkdir event_registration && cd event_registration`
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate`

# Install Django

```bash
pip install django
pip freeze > requirements.txt
```

# Start a Django Project and App

```bash
django-admin startproject event_system .
python manage.py startapp events
```

# Django Configuration

1. Add 'events' to INSTALLED_APPS in event_system/settings.py.
2. Verify SQLite database configuration in settings.py.

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
