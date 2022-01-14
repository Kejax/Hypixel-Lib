from .exceptions import APIError

ranks = {
    "NONE": None,
    "VIP": "VIP",
    "VIP_PLUS": "VIP+",
    "MVP": "MVP",
    "MVP_PLUS": "MVP+",
    "SUPERSTAR": "MVP++",
    "YOUTUBER": "YOUTUBE",
    "PIG+++": "PIG+++",
    "BUILD TEAM": "BUILDER",
    "HELPER": "HELPER",
    "MODERATOR": "MOD",
    "ADMIN": "ADMIN",
    "SLOTH": "SLOTH",
    "OWNER": "OWNER"
}

def rankname(rank, prefix_raw, monthly_package_rank, new_package_rank, package_rank):
	real_rank = None
	if prefix_raw:
		prefix = re.sub(r"§.", "", prefix_raw)[1:-1]
	    # prefixes all start and end with brackets, and have minecraft color codes, this is to remove color codes and
    	# brackets			real_rank = ranks.get(prefix, prefix)
	elif rank and rank != "NORMAL" and not real_rank:
		real_rank = ranks.get(rank, rank)
	elif (monthly_package_rank and monthly_package_rank != "NONE") and not real_rank:
	    # WHY DOES IT EXIST IF IT'S NONE HYPIXEL WHY
	    real_rank = ranks.get(monthly_package_rank, monthly_package_rank)
	elif new_package_rank and not real_rank:
		real_rank = ranks.get(new_package_rank, new_package_rank)
	elif package_rank and not real_rank:
		real_rank = ranks.get(package_rank, package_rank)
	return real_rank
	
class Rank:

	def __init__(self, data):

		self.data = data
		self.name = rankname(
			data.get("player", {}).get("rank"),
			data.get("player", {}).get("prefix"),
			data.get("player", {}).get("monthlyPackageRank"),
			data.get("player", {}).get("newPackageRank"),
			data.get("player", {}).get("packageRank")
			)

