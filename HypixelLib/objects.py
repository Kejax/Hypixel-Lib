import aiohttp
import asyncio
import json

from .exceptions import APIError, NoInputError
from .utils import key_check
from .Mojang import get_uuid
from .hypixelplayer import Player

HYPIXEL_API = "https://api.hypixel.net"


class get_player:

	def __init__(self, api):
		self.api = api


	async def get(self, name=None, uuid=None):

		if name == None and uuid == None:
			raise NoInputError

		if not name == None or not uuid == None:
			
			if uuid == None:
				uuid = await get_uuid(name)

		async with aiohttp.ClientSession() as client:
			async with client.get(f"{HYPIXEL_API}/player?key={self.api}&uuid={uuid}") as response:
				json = await response.json()

		if not json["success"]:

			return None
		else:
			return Player(json)