# Django TODO Application

A simple yet powerful TODO application built with Django, featuring a clean Notion-like UI with vanilla JavaScript and CSS.

## Features

- ✅ Create, edit, and delete TODOs
- 📅 Assign due dates to tasks
- ✓ Mark TODOs as resolved/complete
- 🎨 Clean, Notion-inspired UI
- 🔄 Real-time updates without page refresh
- 📱 Responsive design

## Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: Vanilla JavaScript + CSS
- **Database**: SQLite
- **Package Manager**: uv
- **Containerization**: Docker & Docker Compose

## Prerequisites

- Python 3.12+
- uv (Python package manager)
- Docker and Docker Compose (for containerized deployment)

## Installation

### Using uv (Local Development)

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Clone the repository:
```bash
git clone <repository-url>
cd ai-dev-tools-zoomcamp-01-assignment
```

3. (Optional) Set up environment variables:
```bash
cp .env.example .env
# Edit .env to set your SECRET_KEY and other settings
```

4. Install dependencies:
```bash
uv sync
```

5. Run migrations:
```bash
uv run python manage.py migrate
```

6. Create a superuser (optional, for admin access):
```bash
uv run python manage.py createsuperuser
```

7. Run the development server:
```bash
uv run python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Using Docker

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

2. The application will be available at `http://localhost:8000`

3. To stop the application:
```bash
docker-compose down
```

## Usage

### Web Interface

1. Navigate to `http://localhost:8000` in your browser
2. Use the form at the top to create new TODOs
3. Click the checkbox to mark TODOs as complete
4. Use the Edit button to modify existing TODOs
5. Use the Delete button to remove TODOs

### Admin Interface

Access the Django admin panel at `http://localhost:8000/admin` to manage TODOs with full Django admin features.

## API Endpoints

The application provides a RESTful API:

- `GET /api/todos/` - List all TODOs
- `POST /api/todos/create/` - Create a new TODO
- `PUT /api/todos/<id>/update/` - Update a TODO
- `DELETE /api/todos/<id>/delete/` - Delete a TODO

## Project Structure

```
.
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/               # TODO application
│   ├── migrations/
│   ├── templates/
│   │   └── todos/
│   │       └── index.html
│   ├── admin.py
│   ├── models.py
│   ├── tests.py         # Comprehensive test suite
│   ├── urls.py
│   └── views.py
├── manage.py
├── pyproject.toml       # uv project configuration
├── .env.example         # Example environment variables
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Development

### Running Tests

```bash
uv run python manage.py test
```

### Making Migrations

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

## Security

The application follows Django security best practices:

- **Secret Key**: Loaded from environment variable `DJANGO_SECRET_KEY` (falls back to development key for local testing)
- **Debug Mode**: Controlled via `DEBUG` environment variable (defaults to True for development)
- **Allowed Hosts**: Configured via `ALLOWED_HOSTS` environment variable
- **CSRF Protection**: Disabled for API endpoints (consider using Django REST Framework tokens for production)

For production deployment, ensure you:
1. Set a strong `DJANGO_SECRET_KEY`
2. Set `DEBUG=False`
3. Configure `ALLOWED_HOSTS` with your domain names
4. Use HTTPS
5. Consider implementing proper authentication for the API endpoints

## License

This project is licensed under the terms specified in the LICENSE file.
