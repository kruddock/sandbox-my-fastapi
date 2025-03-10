from fastapi import APIRouter, HTTPException
from data.models import Todo
from services.todo import service_dependency
    
router = APIRouter()

@router.get("/todos" , response_model=list)
async def list_todos(service: service_dependency) -> list:
    return service.all()

@router.post("/todos", response_model=dict, status_code=201)
async def create_todo(payload: Todo, service: service_dependency) -> dict:
    id = service.add(payload)
    
    return { "message": f"Todo {id} has been created"}

@router.get("/todos/{id}", response_model=dict)
async def show_todo(id: str, service: service_dependency) -> dict:
    todo = service.show(id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
    
    return todo

@router.put("/todos/{id}", response_model=dict)
async def update_todo(id: str, payload: Todo, service: service_dependency) -> dict:
    todo = service.update(id, payload)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
    
    return todo

@router.delete("/todos/{id}", status_code=204)
async def delete_todo(id: str, service: service_dependency) -> None:
    todo = service.remove(id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="To do item not found")
