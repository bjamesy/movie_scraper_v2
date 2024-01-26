from fastapi import APIRouter
from src.scrapers.theatre_scraper import (
    get_revue,
    get_tiff,
    get_fox,
    get_paradise,
    get_kingsway,
    get_hotdocs,
    get_imagine_cinemas
)

router = APIRouter()

@router.get("/")
async def get_screenings():
    # res = get_imagine_cinemas("https://imaginecinemas.com/cinema/market-square/")
    res = get_imagine_cinemas("https://imaginecinemas.com/cinema/carlton/")

    return res
