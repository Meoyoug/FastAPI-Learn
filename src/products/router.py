from fastapi import APIRouter, Path, Query

router = APIRouter(prefix="/products", tags=["Products"])

Products = [
    {"id": 1, "name": "IPhone 16 Pro", "price": 1800000},
    {"id": 2, "name": "IPhone 16 Pro MAX", "price": 2000000},
    {"id": 3, "name": "IMac 16inch", "price": 2400000},
]


@router.get("/")
def get_products(max_price: int | None = Query(default=None, ge=100)):
    if max_price is not None:
        results = [product for product in Products if product["price"] <= max_price]
        if results:
            return results
        return {"error": "Product not found"}
    return Products


@router.get("/{product_id}")
def get_product_info(product_id: int = Path(default=..., ge=1)):
    for product in Products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}


@router.get("/search")
def get_product_info(product_name: str = Query(default=..., max_length=20)):
    results = [product for product in Products if product_name in product["name"]]
    if results:
        return results
    return {"error": "Product not found"}
