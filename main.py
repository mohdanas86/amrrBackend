from fastapi import FastAPI
from routers import users, wallet, transactions, health

app = FastAPI(
    title="AMRR Wallet Management API",
    description="A wallet management system with user management and transaction tracking",
    version="1.0.0"
)

# Include all routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(wallet.router)
app.include_router(transactions.router)