import json
import logmsg

replist = {}


def Handle(Name, action):
    if action == "add":
        o = checkrep(Name)
        if o == "Error":
            addentry(Name)
            addMessage(Name)
        else:
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
            replist = json.load(json_file)
            return replist
    except json.decoder.JSONDecodeError:
        addentry("Placeholder")
    except FileNotFoundError:
        try:
            f = open("messageCount.json", "w+")
            f.close()
        except:
            logmsg.logmsg(
                "Cant create File for messages! Please create it manually with the filename (exactly like this!!!!): messageCount.json")


def addMessage(Name):
    replist = loadfromjson()
    if Name in replist:
        u = replist[Name]
        u = int(u)
        u = u+1
        replist[Name] = u
        savetojson(replist)
    else:
        return "Error"


def removeMessage(Name):
    replist = loadfromjson()
    if Name in replist:
        u = replist[Name]
        u = int(u)
        u = u-1
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
    replist[Name] = 0
    savetojson(replist)
    return "done"
