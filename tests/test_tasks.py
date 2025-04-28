import pytest
from fastapi.testclient import TestClient
from main import app, Task, TaskCreate

client = TestClient(app)


@pytest.fixture
def sample_task():
    return TaskCreate(
        title='Sample task',
        description='This is a sample task',
        completed=False,
    )

def test_task_create(sample_task):
    response = client.post("/tasks/", json=sample_task.dict())
    assert response.status_code == 201, 'Task creation failed'
    data = response.json()
    assert data['title'] == 'Sample task', 'Task title does not match'
    assert data['description'] == 'This is a sample task', 'Task description does not match'
    assert data['completed'] == False, 'Task completion status does not match'


def test_task_read(sample_task):
    response = client.post("/tasks/", json=sample_task.dict())
    task_id = response.json()['id']

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200, 'Task read failed'
    data = response.json()
    assert data['title'] == 'Sample task', 'Task title does not match'
    assert data['description'] == 'This is a sample task', 'Task description does not match'
    assert data['completed'] == False, 'Task completion status does not match'


def test_task_update(sample_task):
    response = client.post("/tasks/", json=sample_task.dict())
    task_id = response.json()['id']

    update_data = {"title": "Updated task", "description": "This task has been updated", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200, 'Task update failed'
    data = response.json()
    assert data['title'] == 'Updated task', 'Task title update failed'
    assert data['description'] == 'This task has been updated', 'Task description update failed'
    assert data['completed'] == True, 'Task completion status update failed'


def test_task_delete(sample_task):
    response = client.post("/tasks/", json=sample_task.dict())
    task_id = response.json()['id']

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200, 'Task deletion failed'

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404, 'Task deletion failed, task is still available'