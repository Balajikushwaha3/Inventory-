import sys
import os

# Ye line Python ko batati hai ki isi folder mein 'app' ko dhoondhe
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from app.routers import item_router
# ... baaki code

# Ye command automatic database file aur tables bana degi
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management - User Module")

app.include_router(item_router.router)

@app.get("/")
def read_root():
    return {"message": "API is running", "docs": "/docs"}