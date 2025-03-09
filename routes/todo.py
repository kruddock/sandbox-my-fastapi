from fastapi import APIRouter
    
router = APIRouter()

@router.get("/todos")
async def list_todos():
    return {"action": "List of todos"}

@router.get("/todos/{id}")
async def show_recipe(id: str):
    return {"action": f"Show Todo with id => {id}"}

@router.post("/todos")
async def create_recipe():
    return {"action": "Create Todo with data (from body)"}

@router.put("/todos/{id}")
async def update_recipe(id: str):
    return {"action": "Update Todo with data (from body)"}

@router.delete("/todos")
async def delete_recipe(id: str):
    return {"action": f"Delete Todo with id => {id}"}