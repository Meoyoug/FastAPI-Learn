from typing import Annotated
from fastapi import APIRouter

router = APIRouter(prefix="/products")

fake_items_db = [{"item_name": "1st"}, {"item_name": "2nd"}, {"item_name": "3rd"}]


# Query Parameter
@router.get("")
def read_item(skip: int = 0, limit: int = 10):  # type annotation
    return fake_items_db[skip:skip + limit]


# Query Parameter
@router.get("/{item_id}")
def search_item(item_id: int, q: str | None = None):  # type annotation
    if q:
        return {"item_id": item_id, "q": q}
    return fake_items_db[item_id]


# Annotated
@router.get("/{name}")
def get_product(name: Annotated[str, "제품의 이름 입력"]):
    return {"product": name}