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
 

