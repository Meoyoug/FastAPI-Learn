from typing import Annotated
from fastapi import FastAPI, Query, Path

from schemas import User

app = FastAPI()

fake_items_db = [{"item_name": "1st"}, {"item_name": "2nd"}, {"item_name": "3rd"}]


@app.get("/")
def index():
    return {"msg": "Hello World"}


# Path Parameter
@app.get("/greeting/{name}")
def greeting(name):
    return {"msg": f"Welcome {name}! Have a Nice Day!"}


# Query Parameter
@app.get("/items")
def read_item(skip: int = 0, limit: int = 10):  # type annotation
    return fake_items_db[skip:skip + limit]


# Query Parameter
@app.get("/items/{item_id}")
def search_item(item_id: int, q: str | None = None):  # type annotation
    if q:
        return {"item_id": item_id, "q": q}
    return fake_items_db[item_id]


# Annotated
@app.get("/products/{name}")
def get_product(name: Annotated[str, "제품의 이름 입력"]):
    return {"product": name}


@app.get("/users")
def get_user():
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    return {"user_id": user.id, "user_name": user.name, "user_email": user.email}


# Path Parameter Validation
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int = Path(gt=0)):
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    if user_id == user.id:
        return {"user_id": user.id, "user_name": user.name, "user_email": user.email}
    return {"msg": "User not found"}


# Query Parameter Validation
@app.get("/users/info")
def get_user_info(user_id: int = Query(default=1, gt=0)):
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    if user_id == user.id:
        return {"user_id": user.id, "user_name": user.name, "user_email": user.email}
    return {"msg": "User not found"}
