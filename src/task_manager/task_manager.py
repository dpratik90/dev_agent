from .task import Task

class TaskManager:
def __init__(self):
self.tasks = []

def add_task(self, title, description, due_date, status, priority):
task = Task(title, description, due_date, status, priority)
self.tasks.append(task)

def remove_task(self, title):
self.tasks = [task for task in self.tasks if task.title != title]

def update_task(self, title, **kwargs):
for task in self.tasks:
if task.title == title:
for key, value in kwargs.items():
if hasattr(task, key):
setattr(task, key, value)

def list_tasks(self):
for task in self.tasks:
print(task.title)

def filter_tasks(self, by, value):
return [task for task in self.tasks if getattr(task, by) == value]