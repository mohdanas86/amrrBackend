# AMRR Wallet Management API

A FastAPI-based wallet management system for the AMRR TechSols technical assignment.

### Live Preview 
https://amrr-wallet-api.onrender.com/docs

## Assignment Requirements ✅

This project fulfills all the requirements:

1. **List Users API** - `GET /users/` - Fetch all users with wallet balance
2. **Update Wallet API** - `POST /wallet/update/` - Add or deduct money from wallet  
3. **Fetch Transactions API** - `GET /transactions/{user_id}` - Get user's transaction history
4. **FastAPI Framework** - Built using FastAPI (as preferred)
5. **Swagger Documentation** - Available at `/docs`

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API**
   - Swagger UI: http://localhost:8000/docs
   - API Base: http://localhost:8000

## Project Structure

```
amrrBackend/
├── main.py              # FastAPI app with router configuration
├── models.py            # Pydantic data models
├── database.py          # In-memory data storage
├── routers/             # Modular route handlers
│   ├── health.py        # Health check endpoint
│   ├── users.py         # User management endpoints
│   ├── wallet.py        # Wallet operations
│   └── transactions.py  # Transaction endpoints
└── requirements.txt     # Dependencies
```

## API Endpoints

### 1. Health Check
- **GET** `/` - Check API status

### 2. User Management  
- **GET** `/users/` - List all users with wallet balances
- **GET** `/users/{user_id}` - Get specific user details

### 3. Wallet Operations
- **POST** `/wallet/update/` - Update user wallet balance
  ```json
  {
    "user_id": 1,
    "amount": 500.0
  }
  ```

### 4. Transactions
- **GET** `/transactions/{user_id}` - Get user's transaction history

## Sample Data

The API comes with 5 pre-loaded users for testing:
- Anas Alam (ID: 1) - ₹1000
- John Doe (ID: 2) - ₹500  
- Jane Smith (ID: 3) - ₹750
- Alice Johnson (ID: 4) - ₹0
- Bob Wilson (ID: 5) - ₹250

## Testing

Use the Swagger UI at http://localhost:8000/docs to test all endpoints interactively.

## Features

- ✅ Input validation using Pydantic
- ✅ Error handling with proper HTTP status codes
- ✅ Insufficient balance protection
- ✅ Complete transaction audit trail
- ✅ Modular code structure
- ✅ Interactive API documentation

---

**Developer**: Anas Alam  
**Email**: coadanas@gmail.com  
**Assignment**: AMRR TechSols Technical Assessment
