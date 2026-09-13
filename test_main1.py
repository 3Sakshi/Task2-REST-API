from fastapi.testclient import TestClient
from main1 import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Task Management API"


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing FastAPI",
            "completed": False
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["completed"] is False
    assert "id" in data


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_create_task_validation():
    response = client.post(
        "/tasks",
        json={
            "description": "Title is missing",
            "completed": False
        }
    )

    assert response.status_code == 422


def test_malformed_json():
    response = client.post(
        "/tasks",
        content='{"title": "Broken JSON"',
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 422
    
def test_update_task():
    response = client.put(
        "/tasks/1",
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["completed"] is True


def test_update_missing_task():
    response = client.put(
        "/tasks/999",
        json={
            "title": "Missing Task",
            "description": "This task does not exist",
            "completed": False
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_delete_task():
    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"


def test_delete_missing_task():
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"