from fastapi import APIRouter, HTTPException
from data.models import Recipe
from services.recipe import all, add, show, update, remove

router = APIRouter()

@router.get("/recipes", response_model=list)
async def list_recipes() -> list:
    return all()

@router.post("/recipes", response_model=dict, status_code=201)
async def create_recipe(payload: Recipe) -> dict:
    id = add(payload)
    
    return { "message": f"Recipe {id} has been created"}

@router.get("/recipes/{id}", response_model=dict)
async def show_recipe(id: str) -> dict:
    recipe = show(id)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe

@router.put("/recipes/{id}", response_model=dict)
async def update_recipe(id: str, payload: Recipe) -> dict:
    recipe = update(id, payload)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    return recipe

@router.delete("/recipes/{id}", status_code=204)
async def delete_recipe(id: str) -> None:
    recipe = remove(id)
    
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
