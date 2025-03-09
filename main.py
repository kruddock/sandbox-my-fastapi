from fastapi import FastAPI

from routes.recipe import router as recipe_routes
from routes.todo import router as todo_routes

app = FastAPI()

@app.get("/")
def up():
    return {"status": "Api is running"}

app.include_router(recipe_routes)
app.include_router(todo_routes)