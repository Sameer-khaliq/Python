from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

#______Basic GET Route_______
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def welcome():
    return {"Welcome":"Welcome sameer!!1"}

@app.get("/about")
def about():
    return{"app":"ItemsAPI", "version": "1.0", "author":"Sameer"}


#________Path Parameters___________
from fastapi import FastAPI

app = FastAPI()
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User number {user_id}"}

@app.get("/cities/{city_name}")
def get_city(city_name: str):
    return {"city": city_name, "country": "Pakistan"}



#Query Parameters
#Query parameters come after a ? in the URL — used for filtering, searching
from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search(q: str, limit: int = 10):
    return {
        "query": q,
        "limit": limit,
        "results": f"Showing {limit} results for '{q}'"
    }


#POST Route with a Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name:str
    price:int
    stock: bool = True
@app.post("/items")
def create_item(item: Item):
    return{
        "message":"Item created successfully",
        "item": item
    }

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage (a list — resets when server restarts)
items = []

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/items")
def get_all_items():
    return {"items": items, "total": len(items)}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {
    1: {"name": "Laptop", "price": 150000},
    2: {"name": "Phone", "price": 60000},
    3: {"name": "Headphones", "price": 8000},
}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    return items[item_id]



