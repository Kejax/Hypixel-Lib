import aiohttp
import json as JSON
from .exceptions import InvalidPlayerNameError

MOJANG_API = "https://api.mojang.com"

async def get_uuid(name):
	async with aiohttp.ClientSession() as client:
		async with client.get(f"{MOJANG_API}/users/profiles/minecraft/{name}") as response:
			try:
				json = await response.json()
				return json["id"]
			except Exception:
				raise InvalidPlayerNameError
		