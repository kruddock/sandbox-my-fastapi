from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    desc: str
    is_family: bool = False