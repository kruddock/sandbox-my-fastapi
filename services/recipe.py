from data.models import Recipe 

recipes:list[Recipe] = [] 

def all() -> list[Recipe]:
    return recipes

def add(recipe: Recipe) -> Recipe:
    recipes.append(recipe)
    
    return recipe

def show(id: int) -> Recipe | None:
    if(id >= len(recipes)):
        return None
    
    recipe = recipes[id]
    
    return recipe

def update(id: int, recipe: Recipe) -> Recipe | None:
    target = show(id)
    
    if target is None:
        return None
    
    recipes[id] = recipe
    
    return recipe

def remove(id: int) -> Recipe | None:
    target = show(id)
    
    if target is not None:
       recipes.pop(id)
    
    return target