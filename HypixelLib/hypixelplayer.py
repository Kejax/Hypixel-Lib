from .exceptions import APIError
from .games import Bedwars
from .profile import *
import math





class Player:

	def __init__(self, data):

		self.data = data

		self.name = self.data.get("player", {}).get("displayname")
		self.uuid = self.data.get("player", {}).get("uuid")


		#Network statistics, like rank, karma, level, ...
		self.rank = Rank(data)
		self.karma = self.data.get("player", {}).get("karma")
		self.network_experience = self.data.get("player", {}).get("networkExp")
		self.network_level = round((math.sqrt((2 * self.network_experience) + 30625) / 50) - 2.5, 0)	

		#achievements
		self.achievements_count = len(self.data.get("player", {}).get("achievementsOneTime"))
		self.achievements = self.data.get("player", {}).get("achievementsOneTime")

		#times
		self.last_logout = data.get("player", {}).get("lastLogout")
		self.last_login = data.get("player", {}).get("lastLogin")
		self.first_login = data.get("player", {}).get("firstLogin")

		#socialMedia
		self.discord = self.data.get("player", {}).get("socialMedia", {}).get("links", {}).get("DISCORD", None)
		self.twitter = self.data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITTER", None)
		self.youtube = self.data.get("player", {}).get("socialMedia", {}).get("links", {}).get("YOUTUBE", None)
		self.instagram = self.data.get("player", {}).get("socialMedia", {}).get("links", {}).get("INSTAGRAM", None)
		self.twitch = self.data.get("player", {}).get("socialMedia", {}).get("links", {}).get("TWITCH", None)
		
		#Game statistics
		self.bedwars = Bedwars(data)