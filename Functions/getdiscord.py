import requests


def fetch(url):
    return (lambda u: requests.get(url).json())(url)


def data(name):
    linked = True
    data = fetch(f"https://api.slothpixel.me/api/players/{name}")

    try:
        linked = data["links"]["DISCORD"]
        return linked
    except:
        linked = "Error"
        return linked
 
def rank(name):
    data = fetch(f"https://api.slothpixel.me/api/players/{name}")

    try:
        rank = data["rank"]
        return rank

    except:
        return "Error"