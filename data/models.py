from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    desc: str
    is_family: bool = False
    
class Todo(BaseModel):
    title: str
    desc: str | None
    is_completed: bool = False