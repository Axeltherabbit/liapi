# liapi
lichess python api wrapper\
***This is an ALPHA version***\
***README WORK IN PROGRESS***

# install
```
$ git clone https://github.com/Axeltherabbit/liapi
$ cd liapi
$ sudo python setup.py install
```

# How work
liapi is a wrapper, it work through Lichess http api, official documentation [https://github.com/ornicar/lila#http-api]
Any information of the http request return as attribute, if the api don't send something becouse the user has not done yet it, the attribute is equal to `None`, for example if an user have never played a _crazy house_ game or if optional arguments of a request function are `0`.

# userapi
### user
The `class user(username)` collect all information of the request: [https://github.com/ornicar/lila/blob/master/README.md#get-apiuserusername-fetch-one-user].\
The most important attribute is `.Found` it's `1` if the user is found else `0`.

```
from liapi import userapi

us = userapi.user("pietro9800")

# Before doing something check if is the user was found
if us.Found == 1:
    
    # print all attributes
    print(dir(us))
```

### get_user_list
The function `get_user_list(users)` collect all information of the request:[https://github.com/ornicar/lila/blob/master/README.md#post-apiusers-fetch-many-users-by-id].\
It return a dict of class `user(username)`
```
from liapi import userapi

users = userapi.get_user_list("pietro9800,dominoc")

# print all keys
print(users.keys())

for i in users:
    if users[i].Found == 1:
        # print classical elo for each user in the dict
        print("{} elo classical {}".format(users[i].id,
                                           users[i].classical_rating))
```

# teamapi
### team_user
The function \ 
`team_user(teamname,us_for_page=10,page_number=1)` collect all information of the request:[https://github.com/ornicar/lila/blob/master/README.md#get-apiuser-fetch-many-users-from-a-team]\
It return a dict of class `user(username)`\
optional argument:
- us_for_page [default 10]
- page_number [default 1]
```
from liapi import teamapi

team = teamapi.team_user("coders")

for i in team:
    print("{} elo classical {}".format(team[i].id,
                                       team[i].classical_rating))
```
# gamesapi
### gamesdata
The function `gamesdata(username,games_number=10,page_number=1,...)` collect all information of the request: [https://github.com/ornicar/lila#get-apiuserusernamegames-fetch-user-games]\
It return a dict of class `game_info(dict)`\
optional argument:
- games_number [default 10]
- page_number [default 1]
- analysis [default 0]
- moves [default 0]
- opening [default 0]
- movetimes [default 0]
- rated [default 0]
- playing [default 0]
```
from liapi import gamesapi

mygames = gamesapi.gamesdata("pietro9800",analysis=1,opening=1)

# print attributes of mygames
print(dir(mygames))
print()
# print attributes of elements of mygames
print(dir(mygames[next(iter(mygames))]))

# print all keys 
print("\n\n")
print(mygames.keys())
print()

print("page number:{}".format(mygames.currentPage))
for i in mygames:
    print('''game {} - winner: {} \n\
[black: {} - white: {}]'''.format(mygames[i].id,
                                  mygames[i].winner,
                                  mygames[i].black_userId,
                                  mygames[i].white_userId))


```
