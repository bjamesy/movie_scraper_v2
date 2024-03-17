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
    carlton = await get_imagine_cinemas("https://imaginecinemas.com/cinema/carlton/")
    fox = await get_fox()
    revue = await get_revue()
    tiff = await get_tiff()
    paradise = await get_paradise()
    kingsway = await get_kingsway()
    hotdocs = await get_hotdocs()
    imagine = await get_imagine_cinemas("https://imaginecinemas.com/cinema/market-square/")

    return { 
        "fox": fox, 
        "revue": revue, 
        "tiff": tiff, 
        "paradise": paradise, 
        "kinsgway": kingsway, 
        "hotdocs": hotdocs, 
        "imagine": imagine, 
        "carlton": carlton 
    }
