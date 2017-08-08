import json
import requests
from liapi.userapi import *
from liapi.page_data import *

def team_user(teamname,us_for_page,page_number):

        url =  "https://lichess.org/api/user?team="+teamname+"&nb="+str(us_for_page)+"&page="+str(page_number)

        try:
            datajson=requests.get(url).json()
            datajson=json.dumps(datajson)
        except:
            print("ERROR: team_user except")
            return

        j=json.loads(datajson)

        us_list=page_data(j["paginator"])

        sz=len(j["paginator"]['currentPageResults'])
        count=0

        while (sz>count):
            tmp=user(json.dumps(j["paginator"]['currentPageResults'][count]),1)
            us_list[tmp.id]=tmp
            count+=1

        return us_list
