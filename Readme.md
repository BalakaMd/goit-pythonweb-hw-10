# Contacts Manager API

This is a REST API for managing contacts, built using FastAPI and SQLAlchemy.

## Key Features

- User registration and authentication
- Create, read, update, and delete contacts
- Search contacts by first name, last name, or email
- Retrieve a list of contacts with upcoming birthdays


## Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Alembic (for database migrations)
- 
## Installation and Setup

1. Clone the repository:
 ```bash
git clone https://github.com/BalakaMd/goit-pythonweb-hw-08
 ```
2. Create and activate a virtual environment:
 ```bash
python -m venv venv source venv/bin/activate # for Linux/Mac
venv\Scripts\activate # for Windows
 ```
3. Install dependencies:
 ```bash
pip install -r requirements.txt
 ```
4. Set up your PostgreSQL database and update the connection string in `database.py`.
5. Run the application:
 ```bash
uvicorn main:app --reload
 ```
6. or Launch the application using Docker Compose:
 ```bash
docker-compose up --build
 ```

The API will be available at `http://localhost:8000`.

## API Documentation

After running the application, Swagger documentation will be available at:
`http://localhost:8000/docs`

## Project Structure

- `main.py`: Main application file with API route definitions
- `app/models/models.py`: SQLAlchemy model definitions
- `app/schemas/schemas.py`: Pydantic models for data validation
- `app/db/database.py`: Database connection settings
