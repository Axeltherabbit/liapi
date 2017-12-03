import json
import requests

class activity():
    def __init__(self, j):

        #interval
        content = ["start", "end"]
        for i in content:
            try:
                self.__dict__["interval_"+i] = j["interval"][i]
            except:
                self.__dict__["interval_"+i] = None

        #games
        games_type = ["chess960",
                      "blitz",
                      "crazyhouse",
                      "antichess",
                      "bullet",
                      "correspondence",
                      "atomic",
                      "rapid",
                      "classical",
                      "racingKings",
                      "horde",
                      "ultraBullet",
                      "threeCheck",
                      "kingOfTheHill"]
        content = ["win", "loss", "draw", "rp"]
        try:
            for i in j["games"]:
                    for t in games_type:
                        for k in content:
                            try:
                                self.__dict__["games_"+t+"_"+k]=j["games"][t][k]
                            except:
                                self.__dict__["games_"+t+"_"+k]=None

        except:
            for t in games_type:
                for k in content:
                    self.__dict__["games_"+t+"_"+k]=None

        #correspondenceMoves
        try:
            self.correspondence_nb = j["correspondenceMoves"]["nb"]
        except:
            self.correspondence_nb = None

        self.correspondence_games = []
        try:
            for i in j["correspondenceMoves"]["games"]:
                self.correspondence_games.append(i)

        except:
            pass

        #tournaments
        try:
            self.tournaments_nb = j["tournaments"]["nb"]
        except:
            self.tournaments_nb = None

        self.tournaments_best = []
        try:
            for i in j["tournaments"]["best"]:
                self.tournaments_best.append(i)
        except:
            pass

        #follows
        try:
            self.follows_nb = j["follows"]["in"]["nb"]
        except:
            self.follows_nb = None

        self.follows=[]
        try:
            for i in j["follows"]["in"]["ids"]:
                self.follows.append(i)
        except:
            pass

        #puzzles
        content = ["win","loss","draw","rp"]
        for i in content:
            try:
                self.__dict__["puzzles_"+i] = j["puzzles"]["score"][i]
            except:
                self.__dict__["puzzles_"+i] = None

        #posts
        self.posts=[]
        try:
            for i in j["posts"]:
                self.posts.append(i)
        except:
            pass


def get_activity(us_name):
    url="https://lichess.org/api/user/{}/activity".format(us_name)

    datajson = requests.get(url).text
    j = json.loads(datajson)

    act_list=[]
    for i in j:
        act_list.append(activity(i))

    return act_list
