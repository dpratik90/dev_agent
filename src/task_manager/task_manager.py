from .task import Task


class TaskManager:
	def __init__(self):
		self.tasks = {}
	
	def add_task(self, id, title, description, due_date, status, priority):
		task = Task(title, description, due_date, status, priority)
		self.tasks[id] = task
	
	def remove_task(self, id):
		if id in self.tasks:
			del self.tasks[id]
		else:
			return 'Task ID not found.'

	def update_task(self, id, **kwargs):
		if id in self.tasks:
			task = self.tasks[id]
			for key, value in kwargs.items():
				if hasattr(task, key):
					setattr(task, key, value)
		return 'Task ID not found.'

	def list_tasks(self):
		return list(self.tasks.values())

	def filter_tasks(self, by, value):
		if hasattr(Task, by):
			return [task for task in self.tasks.values() if getattr(task, by) == value]
		else:
			return 'Invalid attribute'


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, description, due_date, status, priority):
        task = Task(id, title, description, due_date, status, priority)
        self.tasks.append(task)

    def remove_task(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]

    def update_task(self, id, **kwargs):
        for task in self.tasks:
            if task.id == id:
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        setattr(task, key, value)

    def list_tasks(self):
        return [task.__dict__ for task in self.tasks]

    def filter_tasks(self, by, value):
        try:
            return [task.__dict__ for task in self.tasks if getattr(task, by) == value]
        except AttributeError:
            return 'Invalid attribute'


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, id, title, description, due_date, status, priority):
        task = Task(title, description, due_date, status, priority)
        self.tasks[id] = task

    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]

    def update_task(self, id, **kwargs):
        if id in self.tasks:
            task = self.tasks[id]
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)

    def list_tasks(self):
        return list(self.tasks.values())

    def filter_tasks(self, by, value):
        if hasattr(Task, by):
            return [task for task in self.tasks.values() if getattr(task, by) == value]
        else:
            return 'Invalid attribute'


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