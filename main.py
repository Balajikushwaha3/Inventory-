import sys
import os
from fastapi import FastAPI

# Windows path fix
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports (Note: folder ka naam 'databases' hai ya 'database'? 
# Photo mein 'databases' dikh raha hai, isliye wahi use karein)
from app.databases.db import engine, Base
from app.routers import item_router

# Tables create karein
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management System")

# Router include karein
app.include_router(item_router.router)

@app.get("/")
def home():
    return {"message": "Success! Server is running.", "docs": "/docs"}