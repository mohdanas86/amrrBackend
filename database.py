from typing import List
from models import User, Transaction

# In-memory database simulation
users = [
    User(id=1, name="Anas Alam", email="coadanas@gmail.com", phone="8603815050", wallet_balance=1000.0),
    User(id=2, name="John Doe", email="john@example.com", phone="9876543210", wallet_balance=500.0),
    User(id=3, name="Jane Smith", email="jane@example.com", phone="1234567890", wallet_balance=750.0),
]

transactions: List[Transaction] = []
