from fastapi import APIRouter
from src.scrapers.theatre_scraper import (
    get_revue,
    get_tiff
)

router = APIRouter()

@router.get("/")
async def get_screenings():
    res = await get_tiff()

    return res
