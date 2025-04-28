=== FILE: tests/test_models.py ===
from fastapi.testclient import TestClient
from main import app, Task, TaskCreate

client = TestClient(app)

def test_task_model():
    task = Task(id=1, owner_id=1, title='Test task', description='Test task description', completed=False)
    assert task.id == 1
    assert task.owner_id == 1
    assert task.title == 'Test task'
    assert task.description == 'Test task description'
    assert task.completed is False

def test_task_create_model():
    task_create = TaskCreate(title='Test task', description='Test task description', completed=False)
    assert task_create.title == 'Test task'
    assert task_create.description == 'Test task description'
    assert task_create.completed is False

def test_task_model_edge_cases():
    task = Task(id=0, owner_id=0, title='', description='', completed=True)
    assert task.id == 0
    assert task.owner_id == 0
    assert task.title == ''
    assert task.description == ''
    assert task.completed is True

def test_task_create_model_edge_cases():
    task_create = TaskCreate(title='', description='', completed=True)
    assert task_create.title == ''
    assert task_create.description == ''
    assert task_create.completed is True

def test_task_model_error_handling():
    try:
        task = Task(id='a', owner_id='b', title=1, description=2, completed='c')
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError on creating a Task with wrong types"

def test_task_create_model_error_handling():
    try:
        task_create = TaskCreate(title=1, description=2, completed='c')
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError on creating a TaskCreate with wrong types"