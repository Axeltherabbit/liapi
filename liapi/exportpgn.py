import requests
def pgn_exporter(game_id):
    url="https://lichess.org/game/export/{}.pgn".format(game_id)
    return requests.get(url).text
