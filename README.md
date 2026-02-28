# Community Blog Platform

A full-stack community blogging platform with a terminal/hacker aesthetic, built with Django REST Framework and Next.js.

## Prerequisites

- Docker and Docker Compose

## Getting Started

1. Copy the example environment file and adjust values:

   ```bash
   cp .env.example .env
   ```

2. Start all services:

   ```bash
   docker compose up --build
   ```

3. The following services will be available:

   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **PostgreSQL**: localhost:5432
   - **Redis**: localhost:6379

4. Run database migrations:

   ```bash
   docker compose exec backend python manage.py migrate
   ```

5. Seed the initial moderator account:

   ```bash
   docker compose exec backend python manage.py seed_moderator
   ```

## Project Structure

```
├── docker-compose.yml
├── .env.example
├── backend/          # Django REST Framework API
└── frontend/         # Next.js frontend
```
