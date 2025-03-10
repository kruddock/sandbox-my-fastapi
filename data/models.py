from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    desc: str
    is_family: bool = False
    
class Todo(BaseModel):
    title: str
    hours: int
    is_completed: bool = False