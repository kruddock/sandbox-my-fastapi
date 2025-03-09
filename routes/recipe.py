from fastapi import APIRouter
from services.recipe import service_dependency
    
router = APIRouter()

@router.get("/recipes")
async def list_recipes(service: service_dependency):
    service.list_entities()
    return {"action": "List of Recipes"}

@router.get("/recipes/{id}")
async def show_recipe(id: str, service: service_dependency):
    service.show_entity()
    return {"action": f"Show Recipe with id => {id}"}

@router.post("/recipes")
async def create_recipe(service: service_dependency):
    service.add_entity()
    return {"action": "Create Recipe with data (from body)"}

@router.put("/recipes/{id}")
async def update_recipe(id: str, service: service_dependency):
    service.update_entity()
    return {"action": "Update Recipe with data (from body)"}

@router.delete("/recipes")
async def delete_recipe(id: str, service: service_dependency):
    service.delete_recipe()
    return {"action": f"Delete Recipe with id => {id}"}