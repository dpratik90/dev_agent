from datetime import datetime\n\nclass Task:\n\"\"\"The Task class represents a task with a title, description, due_date, status, and priority.\"\"\"\n\ndef __init__(self, title: str, description: str, due_date: str, status: str, priority: str) -> None:\n\"\"\"\nInitializes the Task with the given title, description, due date, status and priority.\n\n:param title: The title of the task\n:param description: A brief description of the task\n:param due_date: The due date of the task in 'YYYY-MM-DD' format\n:param status: The status of the task\n:param priority: The priority of the task\n\"\"\"\nself.title = title\nself.description = description\ntry:\nself.due_date = datetime.strptime(due_date, '%Y-%m-%d')\nexcept ValueError:\nraise ValueError('Incorrect date format, should be YYYY-MM-DD')\nself.status = status\nself.priority = priority

class Task:
    """The Task class represents a task with a title, description, due_date, status, and priority."""
    def __init__(self, title: str, description: str, due_date: str, status: str, priority: str) -> None:
        """
        Initializes the Task with the given title, description, due date, status and priority.

        :param title: The title of the task
        :param description: A brief description of the task
        :param due_date: The due date of the task in 'YYYY-MM-DD' format
        :param status: The status of the task
        :param priority: The priority of the task
        """
        self.title = title
        self.description = description
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Incorrect date format, should be YYYY-MM-DD')
        self.status = status
        self.priority = priority

class Task:
    """The Task class represents a task with a title, description, due_date, status, and priority."""
    def __init__(self, title: str, description: str, due_date: str, status: str, priority: str) -> None:
        """
        Initializes the Task with the given title, description, due date, status and priority.

        :param title: The title of the task
        :param description: A brief description of the task
        :param due_date: The due date of the task in 'YYYY-MM-DD' format
        :param status: The status of the task
        :param priority: The priority of the task
        """
        self.title = title
        self.description = description
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Incorrect date format, should be YYYY-MM-DD')
        self.status = status
        self.priority = priority

class Task:
def __init__(self, title, description, due_date, status, priority):
self.title = title
self.description = description
self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
self.status = status
self.priority = priority