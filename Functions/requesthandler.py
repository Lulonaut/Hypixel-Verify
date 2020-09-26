# https://sky.shiiyu.moe/api/v2/profile/Lulonaut
# https://chrome.google.com/webstore/detail/json-handle/iahnhfdhidomcpggpaimmmahffihkfnj

# TODO: Check active Profile, check Skill avg without progression, check slayers
# Slayers :https://sky.shiiyu.moe/api/v2/slayers/Lulonaut
# Use active Profile and search for total SlayerXP
from Functions import storage
import requests
from Functions import storage

finalprofile = None

def fetch(url):
    return (lambda u: requests.get(url).json())(url)

#Only for testing!
def storecurrentdata(name):
    data = fetch(f"https://sky.shiiyu.moe/api/v2/profile/{name}")

    storage.savetojson(data)


# TODO: implement it returning both slayers and skill avg.
def skillaverage(name):
    data = fetch(f"https://sky.shiiyu.moe/api/v2/profile/{name}")

    data = data['profiles']

    keys = list(data.keys())
    tosearch = []
    for i in range(5):
        try:
            tosearch.append(keys[i])
        except IndexError:
            pass
    for i in tosearch:
        if data[i]['current'] == True:
            global finalprofile
            finalprofile = i
    return data[finalprofile]['data']['average_level_no_progress']


def slayers(name):
    slayerdata = fetch(f"http://sky.shiiyu.moe/api/v2/slayers/{name}")
    slayerdata = slayerdata['profiles'][finalprofile]

    

