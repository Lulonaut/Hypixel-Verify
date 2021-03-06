import json

replist = {}


def Handle(Name, action):
    if action == "add":
        o = checkrep(Name)
        if o == "Error":
            addentry(Name)
        addMessage(Name)
    elif action == "check":
        o = checkrep(Name)
        if o == "Error":
            return "User doesnt exist in database"
        else:
            return o
    elif action == "remove":
        o = checkrep(Name)
        if o == "Error":
            addentry(Name)
            addMessage(Name)
        else:
            removeMessage(Name)


def savetojson(dict):
    with open('messageCount.json', 'w') as fp:
        json.dump(dict, fp)


def loadfromjson():
    try:
        with open('messageCount.json') as json_file:
            return json.load(json_file)
    except json.decoder.JSONDecodeError:
        addentry("Placeholder")

def addMessage(Name):
    replist = loadfromjson()
    if Name in replist:
        u = replist[Name]
        u = int(u)
        u += 1
        replist[Name] = u
        savetojson(replist)
    else:
        return "Error"


def removeMessage(Name):
    replist = loadfromjson()
    if Name in replist:
        u = replist[Name]
        u = int(u)
        u -= 1
        replist[Name] = u
        savetojson(replist)
    else:
        return "Error"


def checkrep(Name):
    replist = loadfromjson()
    try:
        return replist[Name]
    except:
        return "Error"


def addentry(Name):
    replist = loadfromjson()
    replist[Name] = 0
    savetojson(replist)
    return "done"
