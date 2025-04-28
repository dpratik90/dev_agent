from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def read_user(user_id: int):
    pass

@router.post("/")
async def create_user():
    pass