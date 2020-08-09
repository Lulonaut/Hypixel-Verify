import requests
data = None
def fetch(url):
    return (lambda u: requests.get(url).json())(url)


def discordlinked(name):
    global data
    try:
        data = fetch(f"https://api.slothpixel.me/api/players/{name}")
    except:
        print(f"Error contacting API while handling request from {name}")
        return "API_ERROR"

    try:
        linked = data["links"]["DISCORD"]
        return linked
    except:
        print(f"{name} has no linked discord, sending error")
        return "DISCORD_ERROR"
 
def rank(name):

    try:
        rank = data["rank"]
        if rank == "VIP_PLUS":
            return "VIP+"
        elif rank == "MVP_PLUS":
            return "MVP+"
        elif rank == "MVP_PLUS_PLUS":
            return "MVP++"
        return rank

    except:
        print(f"Error while getting rank, maybe {name} is a Youtuber or Staff member?")
        return "RANK_ERROR"

def name(name):
    try:
        name=data["username"]
        return name
    except:
        print(f"Error getting correct name for {name}")
        return "NAME_ERROR"

def guild(name):
    data = fetch(f"https://api.slothpixel.me/api/guilds/{name}")
    gname = None
    try:
        gname = data["name"]
    except:
        return "NOT_IN_GUILD"

    if gname == "In Another World With My Guild":
        return "Gmember"
    else:
        return "notGmember"
