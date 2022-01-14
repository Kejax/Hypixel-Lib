import aiohttp
import json
from .exceptions import InvalidPlayerNameError

MOJANG_API = "https://api.mojang.com"

async def get_uuid(name):
	async with aiohttp.ClientSession() as client:
		async with client.get(f"{MOJANG_API}/users/profiles/minecraft/{name}") as response
			try:
				json = response.json()
				return json["id"]
			except json.decoder.JSONDecodeError:
				raise InvalidPlayerNameError
		