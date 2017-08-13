import json
import requests
from liapi.page_data import *
from liapi.return_objdict import *
from liapi.found_class import *


class game_info(dict):
    def __init__(self, datajson):

        self.Found = 1

        j = json.loads(datajson)
        content = ["id",
                   "rated",
                   "variant",
                   "speed",
                   "perf",
                   "createdAt",
                   "lastMoveAt",
                   "turns",
                   "color",
                   "status",
                   "moves",
                   "winner",
                   "url",
                   "fens"]

        for i in content:
            try:
                self.__dict__[i] = j[i]
            except:
                self.__dict__[i] = None

        # clock
        content = ["initial", "increment", "totalTime"]
        for i in content:
            try:
                self.__dict__[i] = j["clock"][i]
            except:
                self.__dict__[i] = None
        # players white&black
        content = ["userId", "name", "rating", "ratingDiff", "moveCentis"]
        for i in content:
            try:
                self.__dict__["white_"+i] = j["players"]["white"][i]
            except:
                self.__dict__["white_"+i] = None
            try:
                self.__dict__["black_"+i] = j["players"]["black"][i]
            except:
                self.__dict__["black_"+i] = None

        # players white&black analysis results
        content = ["inaccuracy", "mistake", "blunder", "acpl"]
        for i in content:
            try:
                self.__dict__["white_"+i] = \
                    j["players"]["white"]["analysis"][i]
            except:
                self.__dict__["white_"+i] = None
            try:
                self.__dict__["black_"+i] = \
                    j["players"]["black"]["analysis"][i]
            except:
                self.__dict__["black_"+i] = None

        # opening
        content = ["eco", "name", "ply"]
        for i in content:
            try:
                self.__dict__["opening_"+i] = j["opening"][i]
            except:
                self.__dict__["opening_"+i] = None

        # game analysis information
        try:
            self.__dict__["analysis"] = j["analysis"]
        except:
            self.__dict__["analysis"] = None


def extract(url):
    try:
        datajson = json.dumps(requests.get(url).json())
    except:
        print("ERROR datajson except of extract()")

    j = json.loads(datajson)

    us_list = page_data(j)
    sz = len(j["currentPageResults"])
    cnt = 0

    while (sz > cnt):
        game_id = (j['currentPageResults'][cnt]["id"])
        us_list[game_id] = game_info(json.dumps(j['currentPageResults'][cnt]))
        cnt += 1

    return us_list


def gamesdata(username,
              games_number=10,
              page_number=1,
              analysis=0,
              moves=0,
              opening=0,
              movetimes=0,
              rated=0,
              playing=0):
    # information: https://github.com/ornicar/lila/blob/master/README.md

    url = '''https://lichess.org/api/user/\
{}/games?nb={}&page={}&with_analysis={}\
&with_moves={}&with_opening={}&with_movetimes={}&rated={}\
&playing={}'''.format(username,
                      games_number,
                      page_number,
                      analysis,
                      moves,
                      opening,
                      movetimes,
                      rated,
                      playing)

    return extract(url)


def pvp_games(user1,
              user2,
              games_number=10,
              page_number=1,
              analysis=0,
              moves=0,
              opening=0,
              movetimes=0,
              rated=0,
              playing=0):
    # information: https://github.com/ornicar/lila/blob/master/README.md

    url = '''https://lichess.org/api/games/vs/{}/{}?nb={}\
&page={}&with_analysis={}&with_moves={}&with_opening={}\
&with_movetimes={}&rated={}&playing={}'''.format(user1,
                                                 user2,
                                                 games_number,
                                                 page_number,
                                                 analysis,
                                                 moves,
                                                 opening,
                                                 movetimes,
                                                 rated,
                                                 playing)
    return extract(url)


def team_games(team_name,
               games_number=10,
               page_number=1,
               analysis=0,
               moves=0,
               opening=0,
               movetimes=0,
               rated=0,
               playing=0):
    # warning lichess api are slow
    url = '''https://lichess.org/api/games/team/{}?nb={}\
&page={}&with_analysis={}&with_moves={}&with_opening={}\
&with_movetimes={}&rated={}&playing={}'''.format(team_name,
                                                 games_number,
                                                 page_number,
                                                 analysis,
                                                 moves,
                                                 opening,
                                                 movetimes,
                                                 rated,
                                                 playing)

    return extract(url)


def game_id(g_id,
            analysis=0,
            moves=0,
            movetimes=0,
            opening=0,
            fens=0):
    url = '''https://lichess.org/api/game/{}?\
with_analysis={}&with_moves={}&with_movetimes={}\
&with_opening={}&with_fens={}'''.format(g_id,
                                        analysis,
                                        moves,
                                        movetimes,
                                        opening,
                                        fens)

    try:
        datajson = json.dumps(requests.get(url).json())
    except:
        print("ERROR datajson except of game_id()")

    rt = game_info(datajson)
    return rt


def many_games_id(games_id_list,
                  analysis=0,
                  moves=0,
                  movetimes=0,
                  opening=0,
                  fens=0):
    url = '''https://lichess.org/api/games?with_analysis={}\
&with_moves={}&with_movetimes={}&with_opening={}\
&with_fens={}'''.format(analysis,
                        moves,
                        movetimes,
                        opening,
                        fens)

    try:
        datajson = \
                requests.post(url=url, headers=None, data=games_id_list).json()
    except:
        print("ERROR datajson except of many_games_id()")

    games_list = {}
    for i in datajson:
        tmp = game_info(json.dumps(i, default=obj_dict))
        games_list[tmp.id] = tmp

    games_names = games_id_list.split(",")
    nofound_games = set(games_names) - games_list.keys()
    for i in nofound_games:
        games_list[i] = nofound()

    return games_list
