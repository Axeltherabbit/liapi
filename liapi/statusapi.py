import json
import requests
class jdata():
    def __init__(self,j):
        content=["id","name","online","playing"]
        for i in content:
            self.__dict__[i]=j[i]


def userstats(players):
    url="https://lichess.org/api/users/status?ids="+players
    try:
        datajson=json.dumps(requests.get(url).json())
    except:
        print("Error datajson except")
        return 0

    j=json.loads(datajson)
    us_list={}
    for i in j:
        us_list[i["id"]]=jdata(i)
    return us_list
