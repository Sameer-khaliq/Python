# #Pydantic model is way to validate data by validation rules and field constraints

# #lets say we make a class the pydantic will validate it automatically
# from pydantic import BaseModel
# class item(BaseModel):
#     name:str
#     id: int
#     stock: bool = True #default value if value is not provided

# #_______Sample Validation_____
# from pydantic import BaseModel
# class User(BaseModel):
#     name : str
#     age : int
#     email: str

# user1 = User(name='Sameer',age=32,email='sam@gmail.com')
# print(user1)
# user2 = User(name='sam',age='33',email='sam@test.com')  #it will automatically convert string'33' to 33(int)
# print(user2)
# # Invalid data — raises ValidationError
# user3 = User(name="Sara", age="not_a_number", email="sara@test.com")
# # ValidationError: age — value is not a valid integer
# print(user3)


# #____________Accessing Model data_______________
# from pydantic import BaseModel
# class Item(BaseModel):
#     name:str
#     price:float
#     stock: bool = True


# item = Item(name = "laptop", price = 15000.0,stock = True)
# print(item.name)
# print(item.price)
# print(item.model_dump())

# #____________Field Validation & Constraints______________
# from pydantic import BaseModel,Field
# class Product(BaseModel):
#     name:str = Field(...,min_length = 2, max_length = 50)
#     price:float = Field(...,gt = 0)
#     quantity: int = Field(...,ge = 0)
#     #... means the field is required (no default).
# try:
#     p1 = Product(name='pc',price = 1200,quantity = 2)
#     print(p1)
# except Exception as e:
#     print(e)

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()
# class Item(BaseModel):
#     name: str = Field(..., min_length=2, description="Name of the item")
#     price: float = Field(..., gt=0, description="Price in PKR, must be positive")
#     quantity: int = Field(0, ge=0, description="Stock quantity, cannot be negative")

# @app.post("/product")
# def add_product(product: Item):
#     return{"message":"{product} added successfully",
#            "product":product
#            }




# #___________Status Codes in FastAPI___________
# from fastapi import FastAPI
# from pydantic import BaseModel,Field

# app = FastAPI()

# class Item(BaseModel):
#     name : str = Field(...,min_length=2)
#     price : float = Field(...,gt = 0)

# items_db ={}
# next_id = 1


# @app.post("/items",status_code=201)
# def add_items(items = Item):
#     global next_id
#     items_db[next_id] = items.dict()
#     items_db[next_id]["id"] = next_id
#     next_id += 1
#     return items_db[next_id - 1]
# @app.delete("/items/{item_id}", status_code=204)   # 204 No Content
# def delete_item(item_id: int):
#     if item_id in items_db:
#         del items_db[item_id]





