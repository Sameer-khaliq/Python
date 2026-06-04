from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
import time

app = FastAPI(
    title="Items API",
    description="A full items API with Pydantic validation and error handling",
    version="2.0"
)

# --- Middleware ---

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} — {response.status_code} — {duration:.3f}s")
    return response

#______models______
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Item name")
    price: float = Field(..., gt=0, description="Price in PKR, must be positive")
    quantity: int = Field(0, ge=0, description="Stock quantity")
    description: Optional[str] = Field(None, max_length=300)
    in_stock: bool = True


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: Optional[str]
    in_stock: bool

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)
    description: Optional[str] = Field(None, max_length=300)
    in_stock: Optional[bool] = None

#_______In-memory DB_____________

items_db = {}
next_id = 1

#_________routes___________
@app.get("/")
def home():
    return {
        "message": "Welcome to Items API v2",
        "total_items": len(items_db),
        "docs": "/docs"
    }


@app.get("/items", response_model=List[ItemResponse])
def get_all_items(
    limit: int = 10,
    in_stock: Optional[bool] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    all_items = list(items_db.values())

    if in_stock is not None:
        all_items = [i for i in all_items if i["in_stock"] == in_stock]

    if min_price is not None:
        all_items = [i for i in all_items if i["price"] >= min_price]

    if max_price is not None:
        all_items = [i for i in all_items if i["price"] <= max_price]

    return all_items[:limit]


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=404,
            detail=f"Item with id {item_id} not found"
        )
    return items_db[item_id]


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new_item = {
        "id": next_id,
        **item.dict()
    }
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_update: ItemUpdate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    existing = items_db[item_id]

    # Only update fields that were actually sent
    update_data = item_update.dict(exclude_unset=True)
    existing.update(update_data)
    items_db[item_id] = existing

    return existing


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    deleted = items_db.pop(item_id)
    return {"message": f"Item '{deleted['name']}' deleted successfully"}