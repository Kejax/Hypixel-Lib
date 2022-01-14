from .objects import *


class Hypixel:

	def __init__(self, api):
		self.api = api
		self.player = get_player(self.api)