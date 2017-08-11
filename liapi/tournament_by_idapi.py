import requests
import json


class tournament_by_id():
    def __init__(self, j):
        content = ["id",
                   "createdBy",
                   "system",
                   "fullName",
                   "nbPlayers",
                   "minutes",
                   "variant",
                   "isStarted",
                   "isFinished",
                   "startsAt",
                   "socketVersion",
                   "pairingsClosed"]

        for i in content:
            try:
                self.__dict__[i] = j[i]
            except:
                self.__dict__[i] = None

        # perf
        content = ["icon", "name"]
        for i in content:
            try:
                self.__dict__["perf_"+i] = j["perf"][i]
            except:
                self.__dict__["perf_"+i] = None

        # clock
        content = ["limit", "increment"]
        for i in content:
            try:
                self.__dict__["clock_"+i] = j["clock"][i]
            except:
                self.__dict__["clock_"+i] = None

        # verdicts
        content = ["list", "accepted"]
        for i in content:
            try:
                self.__dict__["verdicts_"+i] = j["verdicts"][i]
            except:
                self.__dict__["verdicts_"+i] = None

        # schedule
        content = ["freq", "speed"]
        for i in content:
            try:
                self.__dict__["schedule_"+i] = j["schedule"][i]
            except:
                self.__dict__["schedule_"+i] = None

        # stats
        content = ["games",
                   "moves",
                   "whiteWins",
                   "blackWins",
                   "draws",
                   "berserks",
                   "averageRating"]
        for i in content:
            try:
                self.__dict__["stats_"+i] = j["stats"][i]
            except:
                self.__dict__["stats_"+i] = None

        # next
        content = ["id", "name", "nbPlayers", "finishesAt", "startsAt"]
        for i in content:
            try:
                self.__dict__["next_"+i] = j["next"][i]
            except:
                self.__dict__["next_"+i] = None

        # next_perf
        content = ["icon", "name"]
        for i in content:
            try:
                self.__dict__["next_perf_"+i] = j["next"]["perf"][i]
            except:
                self.__dict__["next_perf_"+i] = None

        # podium
        content = ["name",
                   "rank",
                   "rating",
                   "score",
                   "ratingDiff",
                   "performance"]
        for i in content:
            try:
                self.__dict__["podium_first_"+i] = j["podium"][0][i]
            except:
                self.__dict__["podium_first_"+i] = None

            try:
                self.__dict__["podium_second_"+i] = j["podium"][1][i]
            except:
                self.__dict__["podium_second_"+i] = None

            try:
                self.__dict__["podium_third_"+i] = j["podium"][2][i]
            except:
                self.__dict__["podium_third_"+i] = None

        # podium_nb
        content = ["game", "berserk", "win"]
        for i in content:
            try:
                self.__dict__["podium_first_nb_"+i] = j["podium"][0]["nb"][i]
            except:
                self.__dict__["podium_first_nb_"+i] = None

            try:
                self.__dict__["podium_second_nb_"+i] = j["podium"][1]["nb"][i]
            except:
                self.__dict__["podium_second_nb_"+i] = None

            try:
                self.__dict__["podium_third_nb_"+i] = j["podium"][2]["nb"][i]
            except:
                self.__dict__["podium_third_nb_"+i] = None

        # podium_sheet
        content = ["scores", "total", "fire"]
        for i in content:
            try:
                self.__dict__["podium_first_nb_sheet_"+i] = \
                    j["podium"][0]["sheet"][i]

            except:
                self.__dict__["podium_first_nb_sheet_"+i] = None

            try:
                self.__dict__["podium_second_sheet_"+i] = \
                    j["podium"][1]["sheet"][i]

            except:
                self.__dict__["podium_second_sheet_"+i] = None

            try:
                self.__dict__["podium_third_sheet_"+i] = \
                    j["podium"][2]["sheet"][i]

            except:
                self.__dict__["podium_third_sheet_"+i] = None

        # pairings
        self.pairings_id = []
        self.pairings_u = []
        self.pairings_s = []
        for i in j["pairings"]:
            self.pairings_id.append(i["id"])
            self.pairings_u.append(i["u"])
            self.pairings_s.append(i["s"])

        # standing
        self.standing_page = j["standing"]["page"]

        self.standing_name = []
        self.standing_rank = []
        self.standing_rating = []
        self.standing_score = []
        self.standing_ratingDiff = []
        self.standing_sheet = []
        for i in j["standing"]["players"]:
            self.standing_name.append(i["name"])
            self.standing_rank.append(i["rank"])
            self.standing_rating.append(i["rating"])
            self.standing_score.append(i["score"])
            self.standing_ratingDiff.append(i["ratingDiff"])
            self.standing_sheet.append(i["sheet"])


def get_one_tournament(t_id, page=1):
    url = "https://lichess.org/api/tournament/{}?page={}".format(t_id, page)
    datajson = json.dumps(requests.get(url).json())
    j = json.loads(datajson)

    rt = tournament_by_id(j)
    return rt
