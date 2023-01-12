import requests
from bs4 import BeautifulSoup
import csv

november = "https://www.basketball-reference.com/leagues/NBA_2023_games-november.html"

response = requests.get(november)

soup = BeautifulSoup(response.text, 'html.parser')

team_stats_rows = soup.find_all('tr')
away_team_list = list()
away_points_list = list()
home_team_list = list()
home_points_list = list()
margin_list = list()

for row in team_stats_rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        away_team_list.append(cols[1].text)
        away_points_list.append(cols[2].text)
        home_team_list.append(cols[3].text)
        home_points_list.append(cols[4].text)
        margin_list.append(int(cols[2].text) - int(cols[4].text))

with open('schedule.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    for away_team, away_team_points, home_team, home_team_points, margin in zip(away_team_list, away_points_list, home_team_list, home_points_list, margin_list):
        writer.writerow([away_team, away_team_points, home_team, home_team_points, margin])