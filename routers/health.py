from fastapi import APIRouter
from database import users, transactions

router = APIRouter(tags=["Health"])

@router.get("/")
def root():
    """Health check endpoint to verify API is running"""
    return {
        "message": "AMRR Wallet Management API is running!",
        "version": "1.0.0",
        "status": "healthy",
        "total_users": len(users),
        "total_transactions": len(transactions)
    }
