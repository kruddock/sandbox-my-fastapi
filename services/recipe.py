from typing import Final
from bson import ObjectId

from data.models import Recipe
from data.dto import recipe_to_dict, recipes_to_list
from repository.db import database

COLLECTION_NAME: Final[str] = "recipes"
collection = database.get_collection(COLLECTION_NAME)

def all() -> list:
    return recipes_to_list(collection.find())

def add(payload: Recipe) -> str:
    results = collection.insert_one(dict(payload))
    
    return str(results.inserted_id)

def show(id: str) -> dict | None:
    query = { "_id" : ObjectId(id) }
    
    recipe = collection.find_one(query)
    
    return recipe_to_dict(recipe) if recipe is not None else None

def update(id: str, payload: Recipe) -> dict | None:
    query = { "_id" : ObjectId(id) }
    
    data = { "$set" : dict(payload) }

    recipe = collection.find_one_and_update(query, data, return_document=True)
    
    return recipe_to_dict(recipe) if recipe is not None else None

def remove(id: str) -> dict | None:
    query = { "_id" : ObjectId(id) }
     
    recipe = collection.find_one_and_delete(query)
    
    return recipe_to_dict(recipe) if recipe is not None else None
