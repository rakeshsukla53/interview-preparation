
import requests

print requests.utils.default_user_agent()

daily_scoreboard_url = 'http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate=01/12/2016'
scoreboard_response = requests.get(daily_scoreboard_url)



# here you need to give agent a request a user agent!
#
# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'}
# scoreboard_response = requests.get(daily_scoreboard_url, headers=headers)
# print scoreboard_response




