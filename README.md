=== FILE: Dockerfile ===
```docker
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=5000"]
```

=== FILE: requirements.txt ===
```txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
python-multipart
```

=== FILE: /app/main.py ===
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Task Management API!"}
```

=== FILE: /app/database.py ===
```python
from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://user:password@localhost/db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
```

=== FILE: /app/models.py ===
```python
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from app.database import metadata

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(200)),
    Column("userid", None, ForeignKey('users.id'))
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True),
    Column("password", String(100)),
)
```

=== FILE: /app/schemas.py ===
```python
from typing import List, Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
```


=== FILE: /app/auth.py ===
```python
```

=== FILE: /app/crud.py ===
```python
```

=== FILE: /app/utils.py ===
```python
```
Please note that several files such as auth.py, crud.py and utils.py are left blank as they are complex and need a lot of detailed information specific to your application. You need to fill them by yourself as per your need.