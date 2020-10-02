import storage
import requests

# TODO: Altes Monitor Kabel bei neuem verwenden-> NVIDIA Control Panel -> Change resolution -> Output Dynamic range

def fetch(url):
    return (lambda u: requests.get(url).json())(url)

# Only for testing!


def storecurrentdata(name):
    data = fetch(f"https://sky.shiiyu.moe/api/v2/profile/{name}")

    storage.savetojson(data)


def tryhardyesno(name):
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
            finalprofile = i
            pass


# TODO: return true/false for meeting reqs (see tryhardyesno())
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
            pass
    return data[finalprofile]['data']['average_level_no_progress']


def slayers(name):
    slayerdata = fetch(f"http://sky.shiiyu.moe/api/v2/slayers/{name}")
    slayerdata = slayerdata['profiles'][finalprofile]
    #slayerdata = storage.loadfromjson()
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
        return True
    else:
        return False


testsubject = "Lulonaut"
print(skillaverage(testsubject))
print(slayers(testsubject))
