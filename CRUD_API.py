from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Pen", "done": True},
    {"id": 2, "title": "Book", "done": False},
    {"id": 3, "title": "Eraser", "done": True}
]

@app.get("/")
async def get():
  return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
async def get_health():
  return {"status": "ok"}


@app.get("/tasks")
async def get_tasks():
  return tasks

@app.get("/tasks/{id}")
async def get_tasks_id(id:int):
  for task in tasks:
    if task["id"] == id:
      return task
  return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})