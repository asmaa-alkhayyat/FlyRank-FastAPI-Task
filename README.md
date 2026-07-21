# FlyRank FastAPI Task

A simple CRUD API for managing a to-do list, built with **Python** and **FastAPI**. This project was built as part of the FlyRank AI Internship (Backend AI Engineering track).

The API supports creating, reading, updating, and deleting tasks, and includes interactive documentation via Swagger UI.

## How to Install & Run

1. Clone this repository:
   ```
   git clone https://github.com/asmaa-alkhayyat/FlyRank-FastAPI-Task.git
   ```
2. Navigate into the project folder and create a virtual environment:
   ```
   python -m venv env
   ```
3. Activate the environment:
   - Windows: `.\env\Scripts\Activate.ps1`
4. Install the dependencies:
   ```
   pip install fastapi uvicorn
   ```
5. Run the server:
   ```
   uvicorn CRUD_API:app --reload
   ```
6. Open your browser at `http://localhost:8000` to confirm the server is running.

## Endpoints

| Method | Endpoint         | Description                                  |
|--------|------------------|-----------------------------------------------|
| GET    | `/`              | Returns basic info about the API              |
| GET    | `/health`        | Health check — confirms the server is running |
| GET    | `/tasks`         | Returns the full list of tasks                |
| GET    | `/tasks/{id}`    | Returns a single task by id (404 if not found)|
| POST   | `/tasks`         | Creates a new task (title required)           |
| PUT    | `/tasks/{id}`    | Updates a task's title and/or done status     |
| DELETE | `/tasks/{id}`    | Deletes a task by id                          |

## Example Request

```
curl -i http://localhost:8000/tasks/1
```

```
HTTP/1.1 200 OK
date: Tue, 21 Jul 2026 07:52:17 GMT
server: uvicorn
content-length: 38
content-type: application/json
{"id":1,"title":"Buy Pen","done":true}
```

## Interactive Docs (Swagger UI)

FastAPI automatically generates interactive API documentation at `/docs`, where every endpoint can be tested directly from the browser.

![Swagger UI](screenshots/Full_CRUD.png.png)
