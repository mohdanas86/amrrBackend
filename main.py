from fastapi import FastAPI
from routers import users, wallet, transactions, health

app = FastAPI(
    title="AMRR Wallet Management API",
    description="A wallet management system with user management and transaction tracking",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include all routers
app.include_router(health.router)
app.include_router(users.router)
app.include_router(wallet.router)
app.include_router(transactions.router)

# For Render deployment - ensure port binding
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)