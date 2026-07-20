from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Tasks for stage 2
tasks = [
    {"id": 1, "title": "Pen", "done": True},
    {"id": 2, "title": "Book", "done": False},
    {"id": 3, "title": "Eraser", "done": True}
]

# Class for stage 3
class TaskCreate(BaseModel):
    title: Optional[str] = None

@app.get("/")
async def get():
  return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
 
# Stage 1 
@app.get("/health")
async def get_health():
  return {"status": "ok"}

# Return all tasks
@app.get("/tasks")
async def get_tasks():
  return tasks

# Stage 2 (return task with specific id)
@app.get("/tasks/{id}")
async def get_tasks_id(id:int):
  for task in tasks:
    if task["id"] == id:
      return task
  return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})


# Stage 3
@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    if not task.title or task.title.strip() == "":
        return JSONResponse(status_code=400, content={"error": "title is required and cannot be empty"})
    
    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
    new_task = {"id": new_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task