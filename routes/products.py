from models.db import Session
from models.product import Product

from fastapi import FastAPI, APIRouter, HTTPException


router = APIRouter()


@router.post("/create/")
async def create_product(name: str, price: float, category_id: int, description: str = None,):
    try:
        product = Product(name=name, description=description, price=price, category_id=category_id)
        Session.add(product)
        Session.commit()
        return{"product": product.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

