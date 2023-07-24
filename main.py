from fastapi import FastAPI
from request import get_pin

app = FastAPI()


@app.get("/save/<pin_url: str>")
async def save(pin_url):
    data = await get_pin(url=pin_url)
    return data