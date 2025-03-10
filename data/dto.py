def recipe_to_dict(recipe) -> dict: 
    return {
        "id": str(recipe["_id"]),
        "name" : recipe["name"],
        "desc" : recipe["desc"],
        "is_family": recipe["is_family"]
    }
    
def recipes_to_list(recipes) -> list:
    return [recipe_to_dict(recipe) for recipe in recipes]

def todo_to_dict(todo) -> dict: 
    return {
        "id": str(todo["_id"]),
        "title" : todo["title"],
        "hours" : todo["hours"],
        "is_completed": todo["is_completed"]
    }
    
def todos_to_list(todos) -> list:
    return [todo_to_dict(todo) for todo in todos]