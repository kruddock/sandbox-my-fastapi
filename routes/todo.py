from fastapi import APIRouter, HTTPException
from data.models import Todo
from services.todo import service_dependency
    
router = APIRouter()

@router.get("/todos" , response_model=list[Todo])
async def list_todos(service: service_dependency) -> list[Todo]:
    return service.all()

@router.post("/todos", response_model=Todo)
async def create_todo(payload: Todo, service: service_dependency) -> Todo:
    return service.add(payload)

@router.get("/todos/{id}", response_model=Todo)
async def show_todo(id: int, service: service_dependency) -> Todo:
    todo = service.show(id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
    
    return todo

@router.put("/todos/{id}", response_model=Todo)
async def update_todo(id: int, payload: Todo, service: service_dependency) -> Todo:
    todo = service.update(id, payload)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
    
    return todo

@router.delete("/todos/{id}", response_model=Todo)
async def delete_todo(id: int, service: service_dependency) -> Todo:
    todo = service.remove(id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
    
    return todo