import urllib.request
import json
import player

teamDict = {}
playerDict = {}

def get_feed(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode())

# gets the teams from NHL API
def parse_teams():
    try:
        root = get_feed("https://statsapi.web.nhl.com/api/v1/teams")
        # loop to add teams to teamDict
        for i in range(len(root["teams"])):
            # gets team and team id then adds it to teamDict
            teamDict[root["teams"][i]["name"]] = root["teams"][i]["id"]
    except Exception as e:
        print("Couldn't get feed.\nException:" + e)

# gets roster for a specified team from NHL API
def parse_roster(idNum):
    try:
        root = get_feed("https://statsapi.web.nhl.com/api/v1/teams/"+str(idNum)+"/roster")
        for i in range(len(root["roster"])):
            playerDict[root["roster"][i]["person"]["fullName"]] = root["roster"][i]["person"]["id"]
    except Exception as e:
        print("Couldn't get feed")
        print("https://statsapi.web.nhl.com/api/v1/teams/"+str(idNum)+"/roster")
        print("\nException: " + e)

# searches dictionary of teams
def search_team(dTeam):
    result = -1
    if dTeam in teamDict:
        result = teamDict[dTeam]
    return result

def search_player(dPlayer):
    result = -1
    if dPlayer in playerDict:
        result = playerDict[dPlayer]
    return result

# main method
def main():
    parse_teams()
    desiredTeam = input("What team would you like to look for?: ")
    teamIDnum = search_team(desiredTeam)

    if teamIDnum > 0:
        parse_roster(teamIDnum)
    else:
        print(desiredTeam, "not found")
        quit()

    desiredPlayer = input("What player would you like to look for?: ")
    playerIDnum = search_player(desiredPlayer)

    if playerIDnum > 0:
        player.parsePlayer(playerIDnum)

if __name__ == '__main__':
    main()
