from fastapi import FastAPI
from users.router import router as users_router
from products.router import router as products_router

app = FastAPI()
app.include_router(users_router)
app.include_router(products_router)
