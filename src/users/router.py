from fastapi import APIRouter, Path


Users = [
    {"id": 1, "username": "John"},
    {"id": 2, "username": "Jane"},
    {"id": 3, "username": "Rick"},
    {"id": 4, "username": "Kevin"},
]

router = APIRouter(prefix="/users", tags=["Users"])


# 127.0.0.1:8000/users
@router.get("/")
def get_users_handler():
    return Users


# 127.0.0.1:8000/users/1
@router.get("/{user_id}")
def get_user_info_handler(user_id: int = Path(default=..., ge=1)):
    user = next((user for user in Users if user["id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}
