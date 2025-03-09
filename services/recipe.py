from data.models import Recipe 

recipes:list[Recipe] = [] 

def all():
    return recipes

def add(recipe: Recipe):
    recipes.append(recipe)
    return recipe

def show(id: int):
    if(id >= len(recipes)):
        return None
    
    recipe = recipes[id]
    
    return recipe

def update(id: int, recipe: Recipe):
    target = show(id)
    
    if target is None:
        return None
    
    recipes[id] = recipe
    
    return recipe

def remove(id: int):
    target = show(id)
    
    if target is not None:
       recipes.pop(id)
    
    return target