# Hosting App with Database

## About This Project

This project was created to help me learn how to deploy a Django application with a database and understand how uploaded data behaves in production.

The application is a simple blog app where an admin uploads posts through the Django admin panel for users to view and interact with.

---

# Hosting Process

## 1. Configure `settings.py`

Before deployment, several changes need to be made in `settings.py`.

### Move Sensitive Data to `.env`

All sensitive information should be stored inside a `.env` file instead of directly in the project.

Examples include:

- `SECRET_KEY`
- `ALLOWED_HOSTS`
- Database credentials
- API keys and other sensitive settings

---

### Add WhiteNoise Middleware

`WhiteNoise` is used to handle static files in production.

Add it immediately below `SecurityMiddleware` in the `MIDDLEWARE` list:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Rest of the middleware
]
```

Static files are handled differently in production compared to development, which is why `WhiteNoise` is needed.

---

## 2. Upload the Project to GitHub

After making the required changes, push the project to GitHub.

This allows the hosting platform to access the project repository during deployment.

---

## 3. Deploy on Render

### Create a PostgreSQL Database

On Render, first create a new PostgreSQL service.

After creation:

- Copy the database URL
- Store it securely in the `.env` file or environment variables

---

### Create a Web Service

Create a new web service connected to the GitHub repository.

During setup, configure:

- The project root directory
- Build command
- Start command

---

# Commands

## Build Command

This command:

- Installs dependencies
- Runs database migrations
- Collects static files for production

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

---

## Start Command

This command starts the Django application using Gunicorn.

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
```

---

# What I Learned

Through this project, I learned:

- How Django behaves in production
- How to use environment variables
- How static files are handled during deployment
- How to connect Django to a PostgreSQL database
- How to deploy a Django application using Render
- Basic production setup using Gunicorn and WhiteNoise