from ..utils import Games
#from .ultimates import ultimates



class Bedwars:

	def __init__(self, data):


		self.name = "Bedwars"
		self.coins = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("coins", 0)

		#Cosmetics
		self.cosmetics = Cosmetics(data)


		#Gamemodes
		self.solo = Solo(data)
		self.duo = Duo(data)
		self.trio = Trio(data)
		self.squad = Squad(data)
		
		#Games
		self.games = Games(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("games_played_bedwars"),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("wins_bedwars"),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("losses_bedwars")
			)
		self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("winstreak")
		
		#Beds
		self.beds = Beds(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("beds_broken_bedwars"),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("beds_lost_bedwars")
			)
		
		#Kills/Deaths
		self.kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("kills_bedwars", 0)
		self.final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("final_kills_bedwars", 0)
		self.void_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("void_kills_bedwars", 0)
		self.void_final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("void_final_kills_bedwars", 0)
		self.deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("deaths_bedwars", 0)
		self.final_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("final_deaths_bedwars", 0)
		self.void_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("void_deaths_bedwars", 0)
		
		#Items
		self.items = Items(data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("items_purchased_bedwars", 0))

		#Resources
		self.resources = Resources(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("iron_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("gold_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("diamond_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("emerald_resources_collected_bedwars", 0)
			)

#Bedwars Solo rounds
class Solo:

	def __init__(self, data):

		self.name = "Solo"

		#Games
		self.games = Games(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_games_played_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_wins_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_losses_bedwars", 0),
			)
		self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_winstreak")

		#Beds
		self.beds = Beds(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eigth_one_beds_broken_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_beds_lost_bedwars", 0)
			)

		#Kills/Deaths
		self.kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_kills_bedwars", 0)
		self.final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_final_kills_bedwars", 0)
		self.void_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_void_kills_bedwars", 0)
		self.void_final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_void_final_kills_bedwars", 0)
		self.deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_deaths_bedwars", 0)
		self.final_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_final_deaths_bedwars", 0)
		self.void_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_void_deaths_bedwars", 0)
		self.void_deaths_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_void_final_deaths_bedwars", 0)

		#Items
		self.items = Items(data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_items_purchased_bedwars", 0))

		#Resources
		self.resources = Resources(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_iron_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_gold_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_diamond_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_one_emerald_resources_collected_bedwars", 0)
			)

class Duo:

	def __init__(self, data):
		self.name = "Duos"

		#Games
		self.games = Games(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_games_played_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_wins_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_losses_bedwars", 0)
			)
		self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_winstreak")

		#Beds
		self.beds = Beds(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_beds_broken_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_beds_lost_bedwars", 0)
			)

		#Kills/Deaths
		self.kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_kills_bedwars", 0)
		self.final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_final_kills_bedwars", 0)
		self.void_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_void_kills_bedwars", 0)
		self.void_final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_void_final_kills_bedwars", 0)
		self.deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_deaths_bedwars", 0)
		self.final_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_final_deaths_bedwars", 0)
		self.void_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_void_deaths_bedwars", 0)
		self.void_deaths_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_void_final_deaths_bedwars", 0)

		#Items
		self.items = Items(data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_items_purchased_bedwars", 0))

		#Resources
		self.resources = Resources(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_iron_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_gold_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_diamond_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("eight_two_emerald_resources_collected_bedwars", 0)
			)

class Trio:
	
	def __init__(self, data):
		self.name = "Trios"

		#Games
		self.games = Games(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_games_played_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_wins_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_losses_bedwars", 0),
			)
		self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_winstreak")

		#Beds
		self.beds = Beds(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_beds_broken_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_beds_lost_bedwars", 0)
			)

		#Kills/Deaths
		self.kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_kills_bedwars", 0)
		self.final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_final_kills_bedwars", 0)
		self.void_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_void_kills_bedwars", 0)
		self.void_final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_void_final_kills_bedwars", 0)
		self.deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_deaths_bedwars", 0)
		self.final_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_final_deaths_bedwars", 0)
		self.void_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_void_deaths_bedwars", 0)
		self.void_deaths_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_void_final_deaths_bedwars", 0)

		#Items
		self.items = Items(data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_items_purchased_bedwars", 0))

		#Resources
		self.resources = Resources(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_iron_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_gold_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_three_diamond_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_threee_emerald_resources_collected_bedwars", 0)
			)

class Squad:
	
	def __init__(self, data):
		self.name = "Squad"

		#Games
		self.games = Games(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_games_played_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_wins_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_losses_bedwars", 0),
			)
		self.winstreak = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_winstreak")

		#Beds
		self.beds = Beds(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_beds_broken_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_beds_lost_bedwars", 0)
			)

		#Kills/Deaths
		self.kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_kills_bedwars", 0)
		self.final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_final_kills_bedwars", 0)
		self.void_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_void_kills_bedwars", 0)
		self.void_final_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_void_final_kills_bedwars", 0)
		self.deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_deaths_bedwars", 0)
		self.final_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_final_deaths_bedwars", 0)
		self.void_deaths = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_void_deaths_bedwars", 0)
		self.void_deaths_kills = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_void_final_deaths_bedwars", 0)

		#Items
		self.items = Items(data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_items_purchased_bedwars", 0))

		#Resources
		self.resources = Resources(
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_iron_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_gold_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_diamond_resources_collected_bedwars", 0),
			data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("four_four_emerald_resources_collected_bedwars", 0)
			)


class Cosmetics:

	def __init__(self, data):

		self.active_trail = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeProjectileTrail", None)
		self.active_topper = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeIslandTopper", None)
		self.active_npc_skin = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeNPCSkin", None)
		self.active_glyph = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeGlyph", None)
		self.active_killmsg = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeKillMessages", None)
		self.active_deathcry = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeDeathCry", None)
		self.active_victorydance = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeVictoryDance", None)
		self.active_spray = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeSprays", None)
		self.active_kill_effect = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("activeKillEffect", None)
		self.all = data.get("player", {}).get("stats", {}).get("Bedwars", {}).get("packages", None)


class Items:

	def __init__(self, items_purchased):

		self.purchased = items_purchased
		


class Resources:

	def __init__(self, _all, iron, gold, diamonds, emeralds):
		
		self.all = _all
		self.iron = iron
		self.gold = gold
		self.diamonds = diamonds
		self.emeralds = emeralds

#Returns the broken/destroyed Beds
class Beds:
	
	def __init__(self, broken, lost):
		self.name = "Beds destroyed/broken"
		self.destroyed = broken
		self.lost = lost


