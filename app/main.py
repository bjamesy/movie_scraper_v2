from fastapi import FastAPI
import router.v1.screenings as screenings

app = FastAPI()

app.include_router(screenings.router)