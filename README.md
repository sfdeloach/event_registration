# Yet Another Django Tutorial

### Project Idea: Event Registration System

**Overview**: Build a system for users to register for events (e.g., workshops or meetups). Users can sign up, create events, and register for others’ events. This project focuses on models with relationships, forms for user input, and authentication/authorization, using SQLite for simplicity.

**Key Features**:

1. **Models and Database (SQLite)**:

   - **Event Model**: Fields for `title` (CharField), `description` (TextField), `date` (DateTimeField), `organizer` (ForeignKey to User).
   - **Registration Model**: Fields for `event` (ForeignKey to Event), `user` (ForeignKey to User), `registered_date` (DateTimeField).
   - **User Model**: Use Django’s `User` model.

2. **Forms**:

   - **Event Form**: `ModelForm` for creating/editing events (`title`, `description`, `date`).
   - **Registration Form**: Simple form to register a user for an event (e.g., select an event).
   - Use built-in auth forms for registration/login.

3. **User Authentication and Authorization**:

   - Require login for creating events or registering (`@login_required`).
   - Only event organizers can edit their events (`event.organizer == request.user`).
   - Users can register for any event but can’t register twice (unique constraint on `Registration`).

4. **Views and Templates**:

   - **Event List View**: Show all upcoming events (`Event.objects.filter(date__gte=timezone.now())`).
   - **Event Detail View**: Show event details and a “Register” button.
   - **User Dashboard**: List user’s events and registrations.
   - **Login/Register/Logout Views**: Minimal auth templates.
   - Use basic Django templates (e.g., table for events).

5. **Testing**:
   - Test model relationships (e.g., creating an event and registration).
   - Test form validation (e.g., past dates rejected for events).
   - Test authentication (e.g., only logged-in users can register).
   - Test authorization (e.g., non-organizers can’t edit events).
   - Test unique constraints (e.g., prevent duplicate registrations).

**Deployment and CI/CD**:

- **Cloud Service**: Use **Render** (free tier, supports Django/SQLite, simpler than AWS) or PythonAnywhere.
- **CI/CD Pipeline**:
  - Use GitHub Actions (similar to above).
  - For Render, add a deploy step:
    ```yaml
    - name: Deploy to Render
      env:
        RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
      run: curl -X POST https://api.render.com/v1/services/<service-id>/deploys -H "Authorization: Bearer $RENDER_API_KEY"
    ```
  - Ensure `requirements.txt` includes `gunicorn` and set `settings.py` for SQLite.

**Why This Project?** It covers model relationships (ForeignKey), forms with validation, and authorization logic, while being simple enough for a learning project. Render’s free tier is beginner-friendly, and CI/CD is easy to set up.
