# DJANGO ENTERPRISE TEMPLATE

Production-ready Django template for building scalable, maintainable backend systems.

## Getting Started with Docker

### 1. Environment Setup
Create a `.env` file from the template:
```bash
cp .env_template .env
```

### 2. Run Application
#### Local Development
To start the development environment with hot-reloading:
```bash
docker-compose -f docker/docker-compose-develop.yaml up --build
```

#### Production
To start the production environment:
```bash
docker-compose -f docker/docker-compose-prod.yaml up --build -d
```

### 3. Database Migrations
Run migrations inside the Docker container. These migrations are required for default Django applications and for **django-silk** profiling tool.
```bash
docker exec -it django poetry run python src/manage.py migrate
```

> **Note:** If you are using a custom user model and want to create it before other migrations, make sure to handle it before running the full migration command. Generally, migrations should be run after the application is started for the first time.

### Running Tests
To run tests inside the Docker container:
```bash
docker exec -it django poetry run pytest
```

# Technologies

Modern, production-proven technology stack focused on reliability, performance, and maintainability.

## Core
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-API-ff1709?logo=django&logoColor=white)

## Async & Background Jobs
![Celery](https://img.shields.io/badge/Celery-5.6-37814A?logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7.1-DC382D?logo=redis&logoColor=white)

## Web & Application Servers
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?logo=gunicorn&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4051B5)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?logo=nginx&logoColor=white)

## Database
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)

## API & Documentation
![OpenAPI](https://img.shields.io/badge/OpenAPI-3-85EA2D?logo=openapiinitiative&logoColor=black)
![drf-spectacular](https://img.shields.io/badge/drf--spectacular-Schema-85EA2D)

## Containerization & Environment
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-Dependencies-60A5FA?logo=poetry&logoColor=white)
![dotenv](https://img.shields.io/badge/.env-Configuration-ECD53F)

## Code Quality & Tooling
![Black](https://img.shields.io/badge/Black-Formatter-000000)
![Ruff](https://img.shields.io/badge/Ruff-Linter-FCC21B)
![Isort](https://img.shields.io/badge/Isort-Imports-1674B1)
![Mypy](https://img.shields.io/badge/Mypy-Typing-2A6DB2)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC)
![Pre--commit](https://img.shields.io/badge/pre--commit-Git%20Hooks-FAB040)

## Project Architecture

The project follows a modular structure designed for scalability and maintainability.

```text
├── docker/                 # Docker configuration (Dockerfiles, compose files)
├── nginx/                  # Nginx configuration for production
├── scripts/                # Utility scripts (linting, type checking)
└── src/                    # Application source code
    ├── apps/               # Django applications
    │   └── core/           # Core application with shared logic/models
    │       ├── api/        # API views and serializers
    │       ├── tests/      # Application-specific tests
    │       └── tasks.py    # Celery tasks
    ├── settings/           # Split settings (base, local, production)
    ├── asgi.py             # ASGI entry point
    ├── celery_app.py       # Celery configuration
    ├── manage.py           # Django management script
    ├── urls.py             # Main URL configuration
    └── wsgi.py             # WSGI entry point
├── pyproject.toml          # Poetry dependencies and tool configuration
└── pytest.ini              # Pytest configuration
```

## Important Considerations

- **Code Quality:** This template uses `Ruff`, `Mypy`, and `Black` to ensure high code quality. Always run the linting scripts before committing changes.
- **Security:** The `.env` file contains sensitive information. Never commit it to the repository. The provided `DJANGO_SECRET_KEY` in `.env_template` is for development only; generate a unique key for production.
- **Celery & Redis:** Ensure Redis is healthy before starting Celery workers. The provided Docker Compose setup handles this via healthchecks.
- **Modular Apps:** Add new functionality by creating new apps in `src/apps/` to keep the codebase organized.
