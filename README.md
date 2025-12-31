Telejournalism REST API

This project is a simple REST API built with FastAPI and PostgreSQL.  
It provides CRUD operations for a news-related domain and demonstrates
database usage, migrations, and API queries.

The project was created as part of an academic assignment.

Technologies used

FastAPI  
SQLAlchemy  
Alembic  
PostgreSQL  
Pydantic  
Uvicorn  

Project structure

app/
  main.py  
  database.py  
  models.py  
  schemas.py  
  routers/
    events.py
    reports.py
    correspondents.py  

alembic/
  versions/

init_db.py  
requirements.txt  

Database initialization

1. Make sure PostgreSQL is running.
2. Set database credentials in your environment or in the config.
3. Run the initialization script:

python init_db.py

This script creates the database and assigns the owner.

Migrations

Initialize and apply migrations using Alembic:

alembic revision --autogenerate -m "initial"
alembic upgrade head

Migrations are used to:
- add new columns
- create indexes
- update schema safely

Running the server

Start the application with:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

API functionality

The API supports:

- Create records
- Read records
- Update records
- Delete records
- Pagination with skip and limit
- Filtering with query parameters
- Sorting
- JOIN queries
- GROUP BY queries
- Search using JSON field and PostgreSQL indexing

Example request

Create a new event:

POST /events/

Body:
{
  "title": "New Event",
  "location": "Yerevan",
  "description": "Example description"
}

Get all events:

GET /events/

Pagination example

GET /events/?skip=0&limit=10

Search example

GET /events/search/?query=earthquake

Notes

All database access is performed through SQLAlchemy.
Alembic is used for schema migrations.
All endpoints are accessible through Swagger UI.

Each development step should be committed to Git according to assignment rules.
