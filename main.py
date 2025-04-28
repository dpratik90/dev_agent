from fastapi import FastAPI
from app.auth.jwt_bearer import JWTBearer
from app.routers import tasks, users

app = FastAPI()

app.include_router(tasks.router, prefix="/task", tags=["task"], dependencies=[Depends(JWTBearer())])
app.include_router(users.router, prefix="/user", tags=["user"])