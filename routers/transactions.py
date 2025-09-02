from fastapi import APIRouter, HTTPException
from typing import List
from models import Transaction
from database import users, transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/{user_id}", response_model=List[Transaction])
def fetch_transactions(user_id: int):
    """Fetch all wallet transactions for a specific user"""
    # First check if user exists
    user_exists = any(user.id == user_id for user in users)
    if not user_exists:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_txns = [txn for txn in transactions if txn.user_id == user_id]
    return user_txns
