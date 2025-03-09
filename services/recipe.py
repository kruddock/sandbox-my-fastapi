from fastapi import Depends
from typing import Annotated

class RecipeService:
    def list_entities(self):
        print(f"Get list")
        
    def show_entity(self):
        print(f"Get entity")
        
    def add_entity(self):
        print(f"Add entity")
        
    def update_entity(self):
        print(f"Update entity")
        
    def delete_entity(self):
        print(f"Delete entity")
        
def get_service():
    return RecipeService()

service_dependency = Annotated[RecipeService, Depends(get_service)]