=== FILE: tests/test_models.py ===
import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_TaskBase_validation():
    # checking with valid data
    task = TaskBase(title="Test Title", description="Test Description", completed=False)
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed == False

    # checking with empty title
    with pytest.raises(ValueError):
        TaskBase(title="", description="Test Description", completed=False)

    # checking with empty description
    with pytest.raises(ValueError):
        TaskBase(title="Test Title", description="", completed=False)

def test_TaskCreate_validation():
    # checking with valid data
    task = TaskCreate(title="Test Title", description="Test Description", completed=False)
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed == False        

    # checking with empty title
    with pytest.raises(ValueError):
        TaskCreate(title="", description="Test Description", completed=False)

    # checking with empty description
    with pytest.raises(ValueError):
        TaskCreate(title="Test Title", description="", completed=False)

def test_Task_validation():
    # checking with valid data
    task = TaskBase(title="Test Title", description="Test Description", completed=False, id=1, owner_id=1)
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed == False
    assert task.id == 1
    assert task.owner_id == 1      

    # checking with empty title
    with pytest.raises(ValueError):
        TaskBase(title="", description="Test Description", completed=False, id=1, owner_id=1)  

    # checking with empty description
    with pytest.raises(ValueError):
        TaskBase(title="Test Title", description="", completed=False, id=1, owner_id=1)

    # checking with negative task id
    with pytest.raises(ValueError):
        TaskBase(title="Test Title", description="Test Description", completed=False, id=-1, owner_id=1)

    # checking with negative owner id
    with pytest.raises(ValueError):
        TaskBase(title="Test Title", description="Test Description", completed=False, id=1, owner_id=-1)