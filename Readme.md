# Contacts Manager API

This is a REST API for managing contacts, built using FastAPI and SQLAlchemy.

## Features

- Create new contacts
- Retrieve a list of all contacts
- Get a contact by ID
- Update existing contacts
- Delete contacts
- Search contacts by name, surname, or email
- Get a list of contacts with birthdays in the next 7 days

## Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

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

The API will be available at `http://localhost:8000`.

## API Documentation

After running the application, Swagger documentation will be available at:
`http://localhost:8000/docs`

## Project Structure

- `main.py`: Main application file with API route definitions
- `models.py`: SQLAlchemy model definitions
- `schemas.py`: Pydantic models for data validation
- `database.py`: Database connection settings
