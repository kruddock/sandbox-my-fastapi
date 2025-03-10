from fastapi import APIRouter, HTTPException
from data.models import Recipe
from services.recipe import all, add, show, update, remove

router = APIRouter()

@router.get("/recipes", response_model=list[Recipe])
async def list_recipes() -> list[Recipe]:
    return all()

@router.post("/recipes", response_model=Recipe)
async def create_recipe(payload: Recipe) -> Recipe:
    recipe = add(payload)
    
    return recipe

@router.get("/recipes/{id}", response_model=Recipe)
async def show_recipe(id: int) -> Recipe:
    recipe = show(id)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe

@router.put("/recipes/{id}", response_model=Recipe)
async def update_recipe(id: int, payload: Recipe) -> Recipe:
    recipe = update(id, payload)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe

@router.delete("/recipes/{id}", response_model=Recipe)
async def delete_recipe(id: int) -> Recipe:
    recipe = remove(id)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe