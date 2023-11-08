from models.category import Category

from fastapi import APIRouter, HTTPException

from models.db import Session

router = APIRouter()


@router.post("/create/")
async def create_category(name: str, description: str = None):
    # try:
    category = Category(name=name, description=description)
    Session.add(category)
    Session.commit()
    return {"category": category.text}
    
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))