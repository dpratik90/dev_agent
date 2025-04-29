from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import models
from .schemas import tasks, users
from .utils import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.startup()


@app.on_event("shutdown")
async def shutdown():
    await database.shutdown()


app.include_router(users.router, prefix="/users")
app.include_router(tasks.router, prefix="/tasks")