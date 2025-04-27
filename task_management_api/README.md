Given the complexity of the task and the specific application structure, it is not possible to generate all the code at once since it would result in a great deal of code. Instead, I will highlight key parts of the application structure, some utility functions, and a few endpoint examples.

Directory structure:

/app
    /models
    /schemas
    /auth
    /CRUD
    /utils
main.py

Below are examples for the `main.py`, `models.py`, `schemas.py`, `crud.py` files followed by JWT authentication, and CRUD operations via FastAPI and PostgreSQL.

`main.py`:

```python
from fastapi import FastAPI

from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Interfaces and ORM model:

`models.py`:

```python
from sqlalchemy import Column, Integer, String
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
```

`schemas.py`:

```python
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
```

CRUD operations:

`crud.py`:

```python
from sqlalchemy.orm import Session

from . import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
```

JWT authentication middleware and utility functions can be created inside `app/auth` and `app/utils` folders respectively. Implementations can vary a lot based on your application's security requirements.

It's worth mentioning that this example doesn't cover integration tests, Docker deployment settings, environment variable management, and other recommended development practices. You will need to implement those yourself or use a project generation tool like FastAPI's full-stack project generator to scaffold a complete application.