import requests
def pgn_exporter(game_id):
    url="https://lichess.org/game/export/"+game_id+".pgn"
    return requests.get(url).text
