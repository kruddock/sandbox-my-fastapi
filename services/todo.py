from fastapi import Depends
from typing import Annotated, Final
from bson import ObjectId

from data.models import Todo
from data.dto import todo_to_dict, todos_to_list
from repository.db import database

COLLECTION_NAME: Final[str] = "todos"
collection = database.get_collection(COLLECTION_NAME)

class TodoService:
    def all(self) -> list:
        return todos_to_list(collection.find())

    def add(self, payload: Todo) -> str:
        results = collection.insert_one(dict(payload))
        
        return str(results.inserted_id)

    def show(self, id: str) -> dict | None:
        query = { "_id" : ObjectId(id) }
    
        todo = collection.find_one(query)
    
        return todo_to_dict(todo) if todo is not None else None

    def update(self, id: str, payload: Todo) -> dict | None:
        query = { "_id" : ObjectId(id) }
    
        data = { "$set" : dict(payload) }

        todo = collection.find_one_and_update(query, data, return_document=True)
    
        return todo_to_dict(todo) if todo is not None else None

    def remove(self, id: str) -> dict | None:
        query = { "_id" : ObjectId(id) }
     
        todo = collection.find_one_and_delete(query)
    
        return todo_to_dict(todo) if todo is not None else None
    
def get_service() -> TodoService:
    return TodoService()

service_dependency = Annotated[TodoService, Depends(get_service)]
    
    
    