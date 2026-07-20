
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
  return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
async def get_health():
  return {"status": "ok"}
