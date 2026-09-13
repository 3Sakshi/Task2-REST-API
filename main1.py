from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks.",
    version="1.0.0"
)


# Request model
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field("", max_length=500)
    completed: bool = False


# Response model
class Task(TaskCreate):
    id: int


# In-memory task storage
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Build a REST API using FastAPI",
        "completed": False
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to the Task Management API"
    }


# 1. Get all tasks
@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks


# 2. Get one task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# 3. Create a task
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_id = max([t["id"] for t in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)

    return new_task


# 4. Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["description"] = task.description
            existing_task["completed"] = task.completed

            return existing_task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# 5. Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )