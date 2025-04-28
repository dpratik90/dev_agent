Setting up such a complete project requires quite a bit of code and setup steps that can't be provided in a single response. However, I'll create a general guidance on the project structure and provide sample code for various files in your project.

## Database environment setup
First, set up your database environment with docker.
```bash
docker run --name postgres-db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:alpine
```
You can replace `postgres-db`, `myuser`, `mypassword`, `mydb` with your own credentials.

## Project Structure
Below is a basic layout of your project.
```
project_folder/
    Dockerfile
    docker-compose.yml
    main.py
    deps.py
    /app/
        __init__.py
        /crud/
            __init__.py
            crud_tasks.py
            crud_users.py
        /models/
            __init__.py
            tasks.py
            users.py
        /schemas/
            __init__.py
            tasks.py
            users.py
        /auth/
            __init__.py
            auth_service.py
        /utils/
            __init__.py
            db_utils.py
            security_utils.py
```

## main.py
In main.py, we'll define FastAPI application and apply JWT token middleware.
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
import some_library

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    ...

@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks
```

## Define the database models under /app/models/
```python
# users.py

from sqlalchemy import Column, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
```

```python
# tasks.py

from sqlalchemy import Boolean, Column, Integer, String
    
class Task(Base):    
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    complete = Column(Boolean, default=False)
```

## Define the response schema under /app/schemas/

```python
# users.py

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id: Optional[int]

class UserLogin(UserBase):
    username: str
    password: str

class User(UserBase):
    username: str
    class Config:
        orm_mode = True
```

```python
# tasks.py

from pydantic import BaseModel

class Task(BaseModel):
    id: int
    description: str
    complete: bool

    class Config:
        orm_mode = True
```

## Authentication
Check for JWT token authentication in /app/auth/
```python
# auth_service.py

from jose import jwt
import time

def create_access_token(data: dict, expires: timedelta = None):
    to_encode = data.copy()
    if expires:
        expire = datetime.utcnow() + expires
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
```

## CRUD operations
Handle CRUD operations and database communication under /app/crud/
```python
# crud_tasks.py

from sqlalchemy.orm import Session
from sqlalchemy import update
from app.models import tasks

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()
```

This is just a basic setup for a FastAPI project with JWT authentication and PostgreSQL integration. Each of the files and code snippets displayed needs to be complemented with the necessary import statements and extra code.