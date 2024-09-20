from fastapi import FastAPI
from routers.users import router  as user_router
from routers.products import router as product_router

app = FastAPI()
app.include_router(user_router)
app.include_router(product_router)

@app.get("/")
def index():
    return {"msg": "Hello World"}


# Path Parameter
@app.get("/greeting/{name}")
def greeting(name):
    return {"msg": f"Welcome {name}! Have a Nice Day!"}






