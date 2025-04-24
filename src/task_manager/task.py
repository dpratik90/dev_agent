from datetime import datetime

class Task:
def __init__(self, title, description, due_date, status, priority):
self.title = title
self.description = description
self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
self.status = status
self.priority = priority