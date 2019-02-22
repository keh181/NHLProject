import urllib.request
import json


teamDict = {}
playerDict = {}

def get_feed(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode())


def parse_teams():
    try:
        root = get_feed("https://statsapi.web.nhl.com/api/v1/teams")
        # loop to add teams to teamDict
        for i in range(len(root["teams"])):
            # gets team and team id then adds it to teamDict
            teamDict[root["teams"][i]["name"]] = root["teams"][i]["id"]
    except Exception as e:
        print("Couldn't get feed")

def parse_roster(idNum):
    try:
        root = get_feed("https://statsapi.web.nhl.com/api/v1/teams/"+str(idNum)+"/roster")
        for i in range(len(root["roster"])):
            playerDict[root["roster"][i]["person"]["fullName"]] = root["roster"][i]["person"]["id"]
    except Exception as e:
        print("Couldn't get feed")
        print("https://statsapi.web.nhl.com/api/v1/teams/"+str(idNum)+"/roster")


def search_team(dTeam):
    result = -1
    if dTeam in teamDict:
        result = teamDict[dTeam]
    return result


def main():
    parse_teams()
    desiredTeam = input("What team would you like to look for?: ")
    idNum = search_team(desiredTeam)

    if (idNum > 0):
        print(str(idNum))
        parse_roster(idNum)
    else:
        print(desiredTeam, "not found")


if __name__ == '__main__':
    main()
