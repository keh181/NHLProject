# Run using python3.
# Could easily be converted to use python2.
# Just switch from using urllib.request to
# the older urllib module. The module was
# split in python3, but the functionality is
# the same.
import urllib.request
import datetime
import json

# Gets the feed using the NHL.com API
def getFeed(url):
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	return json.loads(response.read().decode())

# parses the NHL scoreboard for a given date
def parseScoreboard(date): # YYYY-mm-dd format
	# Tries to get the json feed for the scoreboard on the given date
	try:
		root = getFeed("https://statsapi.web.nhl.com/api/v1/schedule?startDate=" + date + "&endDate=" + date + "&expand=schedule.linescore")
	except Exception as e:
		print("Failed to find feed.")

	# Loop through each game on the scoreboard
	games = root["dates"][0]["games"]
	for game in games:
		# Check to see if the game has been started or not
		state = game["status"]["detailedState"]
		if state == "Scheduled" or state == "Preview":
			time = game["gameDate"].split("T")[1]
			hour = int(time[:2]) + 19 # convert to EST (24-hour time)
			min = time[3:5]
			print(str(hour) + ":" + min + " ET")
		else: # state == "In Progress" or state == "Final"
			print(game["linescore"]["currentPeriodOrdinal"] + " " + game["linescore"]["currentPeriodTimeRemaining"])
		# Print each team and their score
		print(game["teams"]["away"]["team"]["name"] + " " + str(game["teams"]["away"]["score"]))
		print(game["teams"]["home"]["team"]["name"] + " " + str(game["teams"]["home"]["score"]) + "\n")

# Gets all the games from today and prints their scores
if __name__ == "__main__":
	date = (datetime.datetime.now()-datetime.timedelta(hours=6)).strftime("%Y-%m-%d")
	parseScoreboard(date)
