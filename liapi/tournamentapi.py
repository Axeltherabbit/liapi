import requests
import json


class tournaments():
    def __init__(self, j):
        content = ["id",
                   "createdBy",
                   "system",
                   "minutes",
                   "position",
                   "rated",
                   "fullName",
                   "nbPlayers",
                   "private",
                   "secondsToStart",
                   "startsAt",
                   "finishesAt",
                   "status",
                   "schedule",
                   "winner",
                   "conditions"]

        for i in content:
            try:
                self.__dict__[i] = j[i]
            except:
                self.__dict__[i] = None

        content = ["limit", "increment"]
        for i in content:
            try:
                self.__dict__["clock_"+i] = j["clock"][i]
            except:
                self.__dict__["clock_"+i] = None

        content = ["key", "short", "name"]
        for i in content:
            try:
                self.__dict__["variant_"+i] = j["variant"][i]
            except:
                self.__dict__["variant_"+i] = None

        content = ["icon", "name", "position"]
        for i in content:
            try:
                self.__dict__["perf_"+i] = j["perf"][i]
            except:
                self.__dict__["perf_"+i] = None


def get_tournaments(state):
    if state == ("created" or "started" or "finished"):
        url = "https://lichess.org/api/tournament"
        datajson = json.dumps(requests.get(url).json())

        j = json.loads(datajson)

        tournament_list = {}
        for i in j[state]:
            tournament_list[i["id"]] = tournaments(i)
        return tournament_list

    else:
        print(state+" not valid for get_tournaments()")
