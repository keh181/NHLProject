import urllib.request
import datetime
import json
import time

# the number of teams in the NHL at this given time
# put this here so it'll be easy to change code when Seatle joins the league
MAX_TEAMS = 31
teamList = []


def get_feed(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode())


def parse_teams():

    try:
        root = get_feed("https://statsapi.web.nhl.com/api/v1/teams")
    except Exception as e:
        print("Couldn't get feed")

    # loop to add teams to teamLst
    for i in range(0, MAX_TEAMS):
        # gets team and team id then adds it to teamList
        team = (root["teams"][i]["id"], root["teams"][i]["name"])
        teamList.append(team)


def search_team(dTeam):
    result = -1
    # searches the list of tuples and returns team id
    for t in teamList:
        if (not (dTeam in t)):
            continue
        result = t[0]
    # prints only if team is not found
    if result == "":
        print(dTeam, "not found")
        return -1
    return result


def main():
    desiredTeam = input("What team would you like to look for?: ")
    parse_teams()
    idNum = search_team(desiredTeam)

    if (idNum > 0):
        print(idNum)
    else:
        print(desiredTeam, "not found")


if __name__ == '__main__':
    main()
