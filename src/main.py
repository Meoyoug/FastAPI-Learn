from fastapi import FastAPI

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
@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):  # type annotation
    return fake_items_db[skip:skip + limit]