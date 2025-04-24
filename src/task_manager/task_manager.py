# Importing the datetime module to handle dates
import datetime

# Defining a Task class
class Task:
    def __init__(self, title, description, due_date, status, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        
# Defining a TaskManager class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, status, priority):
        new_task = Task(title, description, due_date, status, priority)
        self.tasks.append(new_task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def update_task(self, title, **kwargs):
        for task in self.tasks:
            if task.title == title:
                for key, value in kwargs.items():
                    setattr(task, key, value)

    def list_tasks(self):
        return self.tasks

    def filter_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def filter_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]