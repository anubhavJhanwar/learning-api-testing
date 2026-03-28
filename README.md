# Learning API Testing with Postman

A simple CRUD API built with FastAPI and MySQL. I'm using this project to learn how to test APIs using Postman.

## What this API does

Manages users — you can create, read, update, and delete them.

## Base URL

```
http://localhost:8000
```

## Endpoints

| Method | Endpoint | What it does |
|--------|----------|--------------|
| GET | `/` | Health check |
| POST | `/users/` | Create a new user |
| GET | `/users/` | Get all users |
| GET | `/users/{id}` | Get a user by ID |
| PUT | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |

## Running locally

1. Install dependencies:
   ```bash
   pip install -r crud-api/requirements.txt
   ```

2. Add your database config to `crud-api/.env`

3. Start the server:
   ```bash
   cd crud-api
   uvicorn main:app --reload
   ```

4. Open the interactive docs at `http://localhost:8000/docs`

## Tech Stack

- Python + FastAPI
- MySQL + SQLAlchemy
- Tested with Postman
