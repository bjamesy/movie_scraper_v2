from fastapi import APIRouter
from src.scrapers.theatre_scraper import (
    get_revue,
    get_tiff,
    get_fox,
    get_carlton,
    get_paradise,
    get_kingsway,
    get_hotdocs
)

router = APIRouter()

@router.get("/")
async def get_screenings():
    res = await get_fox()

    return res
