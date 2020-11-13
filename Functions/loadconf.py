import json


def load():
    with open("config.json") as json_file:
        replist = json.load(json_file)
        return replist
