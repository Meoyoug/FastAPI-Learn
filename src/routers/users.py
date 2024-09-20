from schemas import User
from fastapi import APIRouter, Path, Query

router = APIRouter(prefix="/users")


@router.get("")
def get_user():
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    return {"user_id": user.id, "user_name": user.name, "user_email": user.email}


# Path Parameter Validation
@router.get("/{user_id}")
def get_user_by_id(user_id: int = Path(gt=0)):
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    if user_id == user.id:
        return {"user_id": user.id, "user_name": user.name, "user_email": user.email}
    return {"msg": "User not found"}


# Query Parameter Validation
@router.get("/info")
def get_user_info(user_id: int = Query(default=1, gt=0)):
    user = User(id='1', name='John Doe', email='test@example.com', password='password')
    if user_id == user.id:
        return {"user_id": user.id, "user_name": user.name, "user_email": user.email}
    return {"msg": "User not found"}
