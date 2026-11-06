# Day 19 — PostgreSQL Database Connectivity & Student CRUD API

A Django REST Framework practical using **PostgreSQL (not SQLite and not Docker)**.

Includes:
- PostgreSQL connection through `psycopg`
- Student model and Django ORM
- Database migrations
- ModelSerializer with validation
- GET, POST, PUT, PATCH and DELETE API endpoints
- Responsive Student Management dashboard
- Postman collection and automated tests
- Task-wise comments throughout the code

## 1. Requirements

Install these on your computer:
1. Python 3.10 or newer
2. PostgreSQL (Windows installer) — during installation, remember the password you set for the `postgres` user.
3. pgAdmin 4 (normally included with the PostgreSQL installer)
4. VS Code (recommended)

PostgreSQL official downloads: https://www.postgresql.org/download/windows/

**No Docker is used or required.** Django connects directly to the PostgreSQL server installed on your computer.

## 2. Create the database in pgAdmin

1. Open **pgAdmin 4**.
2. Connect to your local PostgreSQL server using the password you created during installation.
3. Right-click **Databases** → **Create** → **Database**.
4. Enter database name: `day18_students`
5. Click **Save**.

Alternative: open the Query Tool and run:
```sql
CREATE DATABASE day18_students;
```
Run this only once. If the database already exists, do not create it again.

## 3. Configure this Django project

1. Extract the ZIP.
2. Open the extracted `day18_postgresql_student_crud` folder in VS Code (the folder containing `manage.py`).
3. In the VS Code terminal, copy the example environment file:

PowerShell:
```powershell
Copy-Item .env.example .env
```

4. Open `.env` and set the password you chose when installing PostgreSQL:

```env
DB_NAME=day18_students
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_HOST=127.0.0.1
DB_PORT=5432
DJANGO_SECRET_KEY=replace-this-with-a-long-random-secret
DJANGO_DEBUG=True
```

Replace `YOUR_POSTGRES_PASSWORD` with your actual PostgreSQL password. Do not include angle brackets. If you created a different PostgreSQL username or port, update those values too.

## 4. Install Python dependencies

Run these commands in the VS Code terminal from the project folder:

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.env\Scripts\Activate.ps1
```

## 5. Verify PostgreSQL connection and create tables

First check Django configuration:
```powershell
python manage.py check
```

Then apply database migrations:
```powershell
python manage.py migrate
```

This creates the Django tables and `students_api_student` table inside your PostgreSQL database.

Optional: verify the connection directly:
```powershell
python manage.py shell -c "from django.db import connection; connection.ensure_connection(); print('PostgreSQL connection successful:', connection.vendor)"
```
Expected vendor: `postgresql`.

## 6. Run the application

```powershell
python manage.py runserver
```

Open:
- Dashboard: http://127.0.0.1:8000/
- Student API: http://127.0.0.1:8000/api/students/
- Django Admin: http://127.0.0.1:8000/admin/

## 7. Test CRUD using the dashboard

- **Create:** fill the form and click Add student.
- **Read:** records load from PostgreSQL when the dashboard opens.
- **Update:** click Edit, change the details and save.
- **Delete:** click Delete and confirm.
- **Search:** filter the displayed records by name, course or email.

Refresh the page after creating a record. The student should still be present because PostgreSQL stores it persistently.

## 8. API endpoints

| Operation | HTTP method | URL |
|---|---|---|
| Create | POST | `/api/students/` |
| Read all | GET | `/api/students/` |
| Read one | GET | `/api/students/<id>/` |
| Update all fields | PUT | `/api/students/<id>/` |
| Update selected fields | PATCH | `/api/students/<id>/` |
| Delete | DELETE | `/api/students/<id>/` |

Example POST JSON:
```json
{
  "name": "Ketan Kirange",
  "age": 21,
  "course": "Computer Engineering",
  "email": "ketan@example.com"
}
```
Successful creation returns `201 Created`.

## 9. Postman and automated tests

Import `postman_collection.json` into Postman. Start by sending GET or POST to `/api/students/`. Use the returned student ID for detail requests.

With PostgreSQL running and `.env` configured:
```powershell
python manage.py test
```

## 10. Common errors

- **Connection refused:** PostgreSQL service is stopped. Open Windows Services, find the PostgreSQL service (for example `postgresql-x64-16`) and start it.
- **Password authentication failed:** Check `DB_PASSWORD` in `.env`.
- **Database does not exist:** Create `day18_students` in pgAdmin.
- **No module named psycopg:** Activate the virtual environment and run `pip install -r requirements.txt`.
- **Relation does not exist:** Run `python manage.py migrate`.
- **Port 5432 already in use:** Another PostgreSQL server may already be running. Use the port of the server you intend to connect to and update `.env`.

## 11. Stop the application

Stop Django with `Ctrl + C` in the terminal. PostgreSQL is managed separately through Windows Services or pgAdmin; there is no Docker container to stop.
