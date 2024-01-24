from fastapi import APIRouter
from src.scrapers.revue import get_revue

router = APIRouter()

@router.get("/")
async def get_screenings():
    res = await get_revue()

    print("GETTING REVUE ", res)

    return True 
