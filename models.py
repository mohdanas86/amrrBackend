from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

# User schema
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    wallet_balance: float = 0.0

# Wallet update schema
class WalletUpdate(BaseModel):
    user_id: int
    amount: float

# Transaction schema
class Transaction(BaseModel):
    transaction_id: int
    user_id: int
    amount: float
    timestamp: datetime = datetime.utcnow()