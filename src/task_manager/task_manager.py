Here we would consider creating 3 different files: `task.py`, `task_manager.py` and `test_task_management.py`.

However due to space limitations, the below is a stripped-down version of what your requirements would look like.

task.py:
```python
from datetime import datetime
from enum import Enum


class Status(Enum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task:
    """A simple Task class"""

    def __init__(self, id: int, title: str, description: str, due_date: datetime, status: Status,
                 priority: Priority):
        """Initializing a new task"""
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority

    def update_status(self, new_status: Status) -> None:
        """Update task status"""
        self.status = new_status

    def update_priority(self, new_priority: Priority) -> None:
        """Update task priority"""
        self.priority = new_priority

    def to_dict(self) -> dict:
        """Convert task to a dictionary"""
        return self.__dict__
```

task_manager.py:
```python
from typing import List, Optional
from task import Task, Status, Priority


class TaskManager:
    """A simple TaskManager class"""

    def __init__(self):
        """Initializing a new task manager"""
        self.tasks = []

    def add_task(self, task: Task) -> None:
        """Add a new task to task manager"""
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Remove a task from task manager"""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task from task manager"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> List[Task]:
        """List all tasks in task manager"""
        return self.tasks

    def filter_tasks(self, status: Status) -> List[Task]:
        """Filter tasks by status"""
        return [task for task in self.tasks if task.status == status]

    def sort_tasks(self) -> List[Task]:
        """Sort tasks by due date"""
        return sorted(self.tasks, key=lambda task: task.due_date)
```

test_task_management.py:
```python
import unittest
from datetime import datetime
from task import Task, Status, Priority
from task_manager import TaskManager


class TestTask(unittest.TestCase):
    """Unit tests for Task class"""

    def setUp(self):
        self.task = Task(id=1, title="task1", description="this is task1",
                         due_date=datetime.now(), status=Status.TODO, priority=Priority.HIGH)

    def test_update_status(self):
        self.task.update_status(Status.DONE)
        self.assertEqual(self.task.status, Status.DONE)

    def test_update_priority(self):
        self.task.update_priority(Priority.LOW)
        self.assertEqual(self.task.priority, Priority.LOW)

    def test_to_dict(self):
        self.assertIsInstance(self.task.to_dict(), dict)


class TestTaskManager(unittest.TestCase):
    """Unit tests for TaskManager class"""

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = Task(id=1, title="task1", description="this is task1",
                    due_date=datetime.now(), status=Status.TODO, priority=Priority.HIGH)
        self.task_manager.add_task(task)
        self.assertEqual(len(self.task_manager.tasks), 1)

    # continue with other method tests....


if __name__ == "__main__":
    unittest.main()
```
To run above test cases, use the command:
```sh
python -m unittest -v test_task_management.py
```
Above codes need actual implementation of methods, error handling and so on. It just provides a template code structure to help you start the project.