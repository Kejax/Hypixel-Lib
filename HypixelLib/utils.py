import requests

HYPIXEL_API = "https://api.hypixel.net"

def key_check(api):
	response = request.get(f"{HYPIXEL_API}/key?key={api}")
	json = response.json()
	if not json["success"]:
		raise InvalidAPIKeyError(api)
	return APIKey


class Games:

	def __init__(self, played, wins, lost):
		self.played = played
		self.wins = wins
		self.lost = lost



class Prestige:

	def __init__(self):
		self.name = "prestige"