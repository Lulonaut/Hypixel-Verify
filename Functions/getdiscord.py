import requests
data = None
def fetch(url):
    return (lambda u: requests.get(url).json())(url)


def data(name):
    global data
    data = fetch(f"https://api.slothpixel.me/api/players/{name}")

    try:
        linked = data["links"]["DISCORD"]
        return linked
    except:
        linked = "Error"
        return linked
 
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
        return "Error"

def name(name):
    try:
        name=data["username"]
        return name
    except:
        return "Api is down"

def guild(name):
    data = fetch(f"https://api.slothpixel.me/api/guilds/{name}")

    try:
        gname = data["name"]
    except:
        return "Api down"
    if gname == "In Another World With My Guild":
        return True
    else:
        return False
