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
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)

    def update_task(self, title, attribute, new_value):
        for task in self.tasks:
            if task.title == title:
                if attribute == 'title':
                    task.title = new_value
                elif attribute == 'description':
                    task.description = new_value
                elif attribute == 'due_date':
                    task.due_date = new_value
                elif attribute == 'status':
                    task.status = new_value
                elif attribute == 'priority':
                    task.priority = new_value

    def list_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Due date: {task.due_date}, Status: {task.status}, Priority: {task.priority}")

    def filter_tasks(self, attribute, value):
        filtered_tasks = [task for task in self.tasks if getattr(task, attribute) == value]
        return filtered_tasks