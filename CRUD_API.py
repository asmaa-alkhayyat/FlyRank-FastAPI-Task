from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Tasks for stage 2
tasks = [
    {"id": 1, "title": "Buy Pen", "done": True},
    {"id": 2, "title": "Buy Book", "done": False},
    {"id": 3, "title": "Buy Eraser", "done": True}
]


# Class for stage 3
class TaskCreate(BaseModel):
    title: Optional[str] = None

# Class for stage 4
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


@app.get("/")
async def get():
  """Returns basic info about this API: name, version, and available endpoints."""
  return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
 
# Stage 1 
@app.get("/health")
async def get_health():
  """Health check endpoint to confirm the server is running."""
  return {"status": "ok"}

# Return all tasks
@app.get("/tasks")
async def get_tasks():
  """Returns the full list of tasks."""
  return tasks

# Stage 2 (return task with specific id)
@app.get("/tasks/{id}")
async def get_tasks_id(id:int):
  """Returns a single task by id, or 404 if it doesn't exist."""
  for task in tasks:
    if task["id"] == id:
      return task
  return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})


# Stage 3
@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    """Creates a new task with the given title. Title is required and cannot be empty."""
    if not task.title or task.title.strip() == "":
        return JSONResponse(status_code=400, content={"error": "title is required and cannot be empty"})
    
    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
    new_task = {"id": new_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task


# Stage 4 (PUT)
@app.put("/tasks/{id}")
async def update_task(task: TaskUpdate, id: int):
    """Updates a task's title and/or done status. At least one field is required."""
    if task.title is None and task.done is None:
        return JSONResponse(status_code=400, content={"error": "must provide title or done"})
    
    for t in tasks:
        if t["id"] == id:
            if task.title is not None:
                t["title"] = task.title
            if task.done is not None:
                t["done"] = task.done
            return t
    
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

  

# Stage 4 (DELETE)
@app.delete("/tasks/{id}", status_code=204)
async def delete_task(id: int):
    """Deletes a task by id."""
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return
        
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})