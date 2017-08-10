import json
import requests
from liapi.return_objdict import *
from liapi.found_class import *

class user():

    def __init__(self,username,multiuser=0):

        if multiuser!=1:
            url = 'https://lichess.org/api/user/'+ username
            try:
                datajson=json.dumps(requests.get(url).json())
            except:
                self.Found=0
                return
        else:
            datajson=username

        self.Found=1
        j=json.loads(datajson)
        #check if user exist in lichess

        #generic info
        content=["username"
                 ,"id",
                 "online",
                 "createdAt"
                 ,"seenAt",
                 "patron",
                 "language",
                 "url",
                 "playing"
                 ,"nbFollowing",
                 "nbFollowers",
                 "title",
                 "engine"]
        for i in content:
            try:
                self.__dict__[i]=j[i]
            except:
                self.__dict__[i]=None

        #game variants list
        games_type=["chess960"
                    ,"blitz"
                    ,"crazyhouse",
                    "antichess",
                    "bullet"
                    ,"correspondence",
                     "puzzle",
                     "atomic",
                     "classical",
                     "racingKings",
                     "horde",
                     "ultraBullet",
                     "threeCheck",
                     "kingOfTheHill"]
        content=["games",
                 "rating"
                 ,"rd",
                 "prog",
                 "prov"]

        for i in games_type:
            for num_content in content:
                try:
                    self.__dict__[i+"_"+num_content]=j["perfs"][i][num_content]
                except:
                    self.__dict__[i+"_"+num_content]=None

        #get profile info
        content=["country","location","bio","firstName","lastName"]
        for i in content:
            try:
                self.__dict__[i]=j["profile"][i]
            except:
                self.__dict__[i]=None

        #playtime info
        content=["total","tv"]
        for i in content:
            try:
                self.__dict__["playTime_"+i]=j["playTime"][i]
            except:
                self.__dict__[i]=None

        content=["all","rated","ai","draw","drawH","loss","lossH","win","winH","bookmark","playing","import","me"]
        for i in content:
            try:
                self.__dict__["count_"+i]=j["count"][i]
            except:
                self.__dict__[i]=None


def get_user_list(users):

    url = 'https://lichess.org/api/users'

    datajson=requests.post(url=url, headers=None, data=users).json()

    us_list={}
    for i in datajson:
        tmp=user(json.dumps(i, default=obj_dict),1)
        us_list[tmp.id]=tmp

    users_names=users.split(",")
    nofound_users = set(users_names) - us_list.keys()
    for i in nofound_users:
        us_list[i]=nofound()

    return us_list
