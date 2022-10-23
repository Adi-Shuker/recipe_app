from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import requests
import db_manager
import json

app = FastAPI()

app.mount("/client", StaticFiles(directory="client"), name="client")


def _filter_recipes(recipes, dairy_free, gluten_free):
    dairy_ingredients = []
    gluten_ingredients = []
    fliter_recipes = []
    if not dairy_free and not gluten_free:
        return recipes
    if dairy_free:
        dairy_ingredients = db_manager.get_dairy_ingredients()
        for recipe in recipes:
            if not any(item in recipe['ingredients'] for item in dairy_ingredients):
                fliter_recipes.append(recipe)
        recipes = fliter_recipes.copy()
        fliter_recipes = []
    if gluten_free:
        gluten_ingredients = db_manager.get_gluten_ingredients()
        for recipe in recipes:
            if not any(item in recipe['ingredients'] for item in gluten_ingredients):
                fliter_recipes.append(recipe)
        recipes = fliter_recipes.copy()
    return recipes


@app.get("/")
async def get_client():
    return FileResponse('client\index.html')


@app.get("/recipes/{ingredient}")
async def search_recipes(ingredient, dairy_free, gluten_free):
    dairy_free = True if dairy_free == 'true' else False
    gluten_free = True if gluten_free == 'true' else False
    ingredient = ingredient.lower()
    recipes = []
    res = requests.get(
        f'https://recipes-goodness.herokuapp.com/recipes/{ingredient}')
    res = list(json.loads(res.text)['results'])
    recipes = list(map(lambda recipe: {
        "title": recipe['title'],
        "thumbnail": recipe['thumbnail'],
        "href": recipe['href'],
        "ingredients": list(map(lambda ingredient: ingredient.lower(), recipe['ingredients']))
    }, res))
    recipes = _filter_recipes(recipes, dairy_free, gluten_free)
    return recipes


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
