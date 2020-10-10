import requests
from Functions import logmsg

testsubject = "Hammerkit"


def fetch(url):
    return (lambda u: requests.get(url).json())(url)


# TODO Comments


def tryhard(name):
    data = fetch(f"https://sky.shiiyu.moe/api/v2/profile/{name}")
    slayerdata = fetch(f"http://sky.shiiyu.moe/api/v2/slayers/{name}")
    try:
        data = data['profiles']
    except:
        tolog = (f"[Tryhard Command] error while resolving request for {name}")
        logmsg.logmsg(tolog)
        # TODO d: Error with your Username or you dont play Skyblock!
        return "d"
    keys = list(data.keys())
    tosearch = []
    for i in range(5):
        try:
            tosearch.append(keys[i])
        except IndexError:
            pass

    for i in tosearch:
        if data[i]['current'] == True:
            finalprofile = i
            pass
    skillavg = data[finalprofile]['data']['average_level_no_progress']
    slayerdata = slayerdata['profiles'][finalprofile]
    sven = slayerdata['slayers']['wolf']['level']['currentLevel']
    tara = slayerdata['slayers']['spider']['level']['currentLevel']
    rev = slayerdata['slayers']['zombie']['level']['currentLevel']

    lvl7 = 0
    sven = int(sven)
    tara = int(tara)
    rev = int(rev)
    if sven > 6:
        lvl7 = lvl7+1

    if tara > 6:
        lvl7 = lvl7+1

    if rev > 6:
        lvl7 = lvl7+1

    if lvl7 >= 2:
        slayers = True
    else:
        slayers = False

    if skillavg >= 30:
        # TODO a: You meet it because your Skill average is higher than/or 30!
        return "a"
    elif skillavg >= 25 and slayers == True:
        # TODO b: You meet it because your Skill average is higher than 25 and you have two Slayers at level 7
        return "b"
    else:
        # TODO c: You dont meet it, sorry!
        return "c"
