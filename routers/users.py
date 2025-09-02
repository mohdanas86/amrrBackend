from fastapi import APIRouter, HTTPException
from typing import List
from models import User
from database import users

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[User])
def list_users():
    """Fetch all users with their details including wallet balance"""
    return users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    """Get details of a specific user by their ID"""
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
