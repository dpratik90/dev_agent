from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_task():
    pass

@router.get("/")
async def read_tasks():
    pass

@router.get("/{task_id}")
async def read_task(task_id: int):
    pass

@router.put("/{task_id}")
async def update_task(task_id: int):
    pass

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    pass