from fastapi import Depends
from typing import Annotated
from data.models import Todo 

class TodoService:
    todos:list[Todo] = []
    
    def all(self) -> list[Todo]:
        return TodoService.todos

    def add(self, todo: Todo) -> Todo:
        TodoService.todos.append(todo)
        
        return todo

    def show(self, id: int) -> Todo | None:
        if(id >= len(TodoService.todos)):
            return None
        
        return TodoService.todos[id]

    def update(self, id: int, recipe: Todo) -> Todo | None:
        target = self.show(id)
    
        if target is None:
            return None
        
        TodoService.todos[id] = recipe
        
        return recipe

    def remove(self, id: int) -> Todo | None:
        target = self.show(id)
        
        if target is not None:
            TodoService.todos.pop(id)
        
        return target
    
def get_service() -> TodoService:
    return TodoService()

service_dependency = Annotated[TodoService, Depends(get_service)]
    
    
    