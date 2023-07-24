import aiohttp
import asyncio
from pydantic import TypeAdapter

from models import Pin

async def get_pin(url) -> Pin:
	async with aiohttp.ClientSession() as session:
		async with session.get(url=f"https://pinterestdownloader.io/frontendService/DownloaderService?url={url}") as response:
			adapter = TypeAdapter(Pin)
			return adapter.validate_python(await response.json())




