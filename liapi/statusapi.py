import json
import requests
from liapi.found_class import *


class jdata():
    def __init__(self, j):
        self.Found=1
        content = ["id", "name", "online", "playing"]
        for i in content:
            self.__dict__[i] = j[i]



def userstats(players):
    url = "https://lichess.org/api/users/status?ids={}".format(players)
    try:
        datajson = json.dumps(requests.get(url).json())
    except:
        print("Error datajson except")
        return 0

    j = json.loads(datajson)
    us_list = {}
    for i in j:
        us_list[i["id"]] = jdata(i)

    us_names = players.split(",")
    nofound_games = set(us_names) - us_list.keys()
    for i in nofound_games:
        us_list[i] = nofound()

    return us_list
