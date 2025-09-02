from fastapi import APIRouter, HTTPException
from models import WalletUpdate, Transaction
from datetime import datetime
from database import users, transactions

router = APIRouter(prefix="/wallet", tags=["Wallet"])

@router.post("/update/")
def update_wallet(wallet: WalletUpdate):
    """Add or deduct amount from a user's wallet"""
    for user in users:
        if user.id == wallet.user_id:
            # Check if user has sufficient balance for negative amounts
            if wallet.amount < 0 and user.wallet_balance + wallet.amount < 0:
                raise HTTPException(status_code=400, detail="Insufficient balance")
            
            user.wallet_balance += wallet.amount
            transaction = Transaction(
                transaction_id=len(transactions) + 1,
                user_id=user.id,
                amount=wallet.amount,
                timestamp=datetime.utcnow()
            )
            transactions.append(transaction)
            return {
                "message": "Wallet updated successfully",
                "user_id": user.id,
                "new_balance": user.wallet_balance,
                "transaction_id": transaction.transaction_id
            }
    raise HTTPException(status_code=404, detail="User not found")
