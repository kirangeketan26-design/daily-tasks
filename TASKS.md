# Day 18 — Task-wise completion checklist

Based on the supplied Day 18 practical sheet.

## Task 1 — Connect Django to PostgreSQL
- Configured Django `DATABASES` with PostgreSQL engine.
- Uses `psycopg` driver.
- Reads database credentials from `.env`.
- Added `docker-compose.yml` to launch PostgreSQL 16 for repeatable local setup.

## Task 2 — Create a Student model
- Implemented `Student` with name, age, course, email, and created_at fields.
- Added model metadata and readable string representation.

## Task 3 — Run database migrations
- Included initial migration `0001_initial.py`.
- Run `python manage.py migrate` to create Django and Student tables in PostgreSQL.

## Task 4 — Create serializers and CRUD API endpoints
- Implemented `StudentSerializer` using `ModelSerializer`.
- Implemented list/create and retrieve/update/partial-update/delete endpoints.
- Added validation and HTTP status handling.

## Task 5 — Test database operations through API requests
- Included automated API tests.
- Included Postman collection.
- Added dashboard UI to exercise all CRUD operations.

## Expected output
- Student CRUD REST API.
- PostgreSQL database connectivity.
- Responsive student management dashboard.
