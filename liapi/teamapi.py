import json
import requests
from liapi.userapi import *
from liapi.page_data import *


def team_user(teamname, us_for_page=10, page_number=1):

        url = '''https://lichess.org/api/user?\
                 team={}&nb={}&page={}'''.format(teamname,
                                                 us_for_page,
                                                 page_number)

        try:
            datajson = requests.get(url).json()
            datajson = json.dumps(datajson)
        except:
            print("ERROR: team_user except")
            return

        j = json.loads(datajson)

        us_list = page_data(j["paginator"])

        sz = len(j["paginator"]['currentPageResults'])
        cnt = 0

        while (sz > cnt):
            tmp = \
               user(json.dumps(j["paginator"]['currentPageResults'][cnt]), 1)
            us_list[tmp.id] = tmp
            cnt += 1

        return us_list
