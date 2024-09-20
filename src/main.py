from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"msg": "Hello World"}


# Path Parameter
@app.get("/greeting/{name}")
def greeting(name):
    return {"msg": f"Welcome {name}! Have a Nice Day!"}
