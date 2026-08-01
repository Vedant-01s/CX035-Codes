from fastapi import FastAPI

app = FastAPI()

# 1. Add this root route so the main URL doesn't throw a 404
@app.get("/")
def read_root():
    return {"status": "Backend is running successfully!"}

# 2. Keep your data endpoints exactly like this so the frontend can read them
@app.get("/api/overview/kpis")
def get_kpis():
    return {
        "revenue": 12.4,
        "sales": 24502,
        "customers": 8402,
        "inventory": 14205
    }

@app.get("/api/sales/recent")
def get_recent_sales():
    return [
        {
            "order_id": "#ORD-9021", 
            "date": "Today, 10:42 AM", 
            "category": "Groceries", 
            "amount": "₹4,500", 
            "status": "Completed"
        }
    ]

@app.get("/api/inventory/stock")
def get_inventory():
    return [
        {
            "product_name": "Sona Masoori Rice (5kg)", 
            "category": "Groceries", 
            "stock": 142, 
            "status": "In Stock"
        }
    ]
