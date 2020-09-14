import urllib.request
import datetime
import json

class Player(object):
    name = ""
    gp = 0
    goals = 0
    assists = 0
    points = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, gp, goals, assists, points):
        self.name = name
        self.gp = gp
        self.goals = goals
        self.assists = assists
        self.points = points

    def printPlayer(self):
        print("Name: " + self.name + "\n Games Played: " + str(self.gp) + "\n Goals: " + str(self.goals) + "\n Assists: " + str(self.assists) + "\n Total Points: " + str(self.points))

def make_player(name, gp, g, a, p):
    player = Player(name,gp,g,a,p)
    return player

def getFeed(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode())

def parsePlayer(playerID):
    try:
        root = getFeed("https://statsapi.web.nhl.com/api/v1/people/" + str(playerID) +"?hydrate=stats(splits=statsSingleSeason)")
    except Exception as e:
        print("Failed to find player")
        print("Exception: " + e)
    #gathering data to make Player object
    playerName = root["people"][0]["fullName"]
    gamesPlayed = root["people"][0]["stats"][0]["splits"][0]["stat"]["games"]
    playerGoals = root["people"][0]["stats"][0]["splits"][0]["stat"]["goals"]
    playerAssists = root["people"][0]["stats"][0]["splits"][0]["stat"]["assists"]
    playerPoints = root["people"][0]["stats"][0]["splits"][0]["stat"]["points"]
    newPlayer = make_player(playerName,gamesPlayed,playerGoals,playerAssists,playerPoints)
    return newPlayer

def main():
    #currently is Sidney Crosby's stats
    parsePlayer(8471675)



if __name__ == '__main__':
    main()
