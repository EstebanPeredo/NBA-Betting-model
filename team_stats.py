import requests
from bs4 import BeautifulSoup
import csv

stats = "https://cleaningtheglass.com/stats/league/fourfactors"

response = requests.get(stats)

soup = BeautifulSoup(response.text, 'html.parser')

team_stats_rows = soup.find_all('tr')

team_names = list()
efficiency_differentials = list()
points_per_100_possessions = list()
effective_fg_percentages = list()
turnover_percentages = list()
offensive_rebound_percentages = list()
free_throw_rates = list()
points_allowed_per_100_possessions = list()
opponents_effective_fg_percentages = list()
opponents_turnover_percentages = list()
opponents_offensive_rebound_percentages = list()
opponents_free_throw_rates = list()

for row in team_stats_rows:
    cols = row.find_all('td')
    if len(cols) > 0:
        team_names.append(cols[1].text)
        efficiency_differentials.append(cols[6].text)
        points_per_100_possessions.append(cols[9].text)
        effective_fg_percentages.append(cols[11].text[:-1])
        turnover_percentages.append(cols[13].text[:-1])
        offensive_rebound_percentages.append(cols[15].text[:-1])
        free_throw_rates.append(cols[17].text)
        points_allowed_per_100_possessions.append(cols[20].text)
        opponents_effective_fg_percentages.append(cols[22].text[:-1])
        opponents_turnover_percentages.append(cols[24].text[:-1])
        opponents_offensive_rebound_percentages.append(cols[26].text[:-1])
        opponents_free_throw_rates.append(cols[28].text)

with open('stats.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerows([])

    writer.writerow(["Team Name", "Efficiency Differential", "Points Per 100 Possestions", "Effective FG%", "TOV%",
                     "Offensive REB%", "Free Throw Rate", "Points Allowed Per 100 Possesions", "Opponent Effective FG%",
                     "Opponent TOV%", "Opponent OREB%", "Opponent Free Throw Rate"])

    for names, ed, pp100, ef, tov, orb, ftr, pap100, oef, otov, oorb, oft in zip(team_names, efficiency_differentials,
                                                                                 points_per_100_possessions,
                                                                                 effective_fg_percentages,
                                                                                 turnover_percentages,
                                                                                 offensive_rebound_percentages,
                                                                                 free_throw_rates,
                                                                                 points_allowed_per_100_possessions,
                                                                                 opponents_effective_fg_percentages,
                                                                                 opponents_turnover_percentages,
                                                                                 opponents_offensive_rebound_percentages,
                                                                                 opponents_free_throw_rates):
        writer.writerow([names, ed, pp100, ef, tov, orb, ftr, pap100, oef, otov, oorb, oft])

with open('stats.csv', 'r') as csv_file:
    modified_rows = []

    for row in csv.reader(csv_file):
        row = [s.replace('Boston', 'Boston Celtics') for s in row]
        row = [s.replace('Memphis', 'Memphis Grizzlies') for s in row]
        row = [s.replace('Cleveland', 'Cleveland Cavaliers') for s in row]
        row = [s.replace('New Orleans', 'New Orleans Pelicans') for s in row]
        row = [s.replace('Philadelphia', 'Philadelphia 76ers') for s in row]
        row = [s.replace('Brooklyn', 'Brooklyn Nets') for s in row]
        row = [s.replace('Phoenix', 'Phoenix Suns') for s in row]
        row = [s.replace('Milwaukee', 'Milwaukee Bucks') for s in row]
        row = [s.replace('Dallas', 'Dallas Mavericks') for s in row]
        row = [s.replace('Denver', 'Denver Nuggets') for s in row]
        row = [s.replace('New York', 'New York Knicks') for s in row]
        row = [s.replace('Sacramento', 'Sacramento Kings') for s in row]
        row = [s.replace('Utah', 'Utah Jazz') for s in row]
        row = [s.replace('Golden State', 'Golden State Warriors') for s in row]
        row = [s.replace('Toronto', 'Toronto Raptors') for s in row]
        row = [s.replace('Portland', 'Portland Trail Blazers') for s in row]
        row = [s.replace('LA Clippers', 'Los Angeles Clippers') for s in row]
        row = [s.replace('Minnesota', 'Minnesota Timberwolves') for s in row]
        row = [s.replace('Miami', 'Miami Heat') for s in row]
        row = [s.replace('Atlanta', 'Atlanta Hawks') for s in row]
        row = [s.replace('Chicago', 'Chicago Bulls') for s in row]
        row = [s.replace('Indiana', 'Indiana Pacers') for s in row]
        row = [s.replace('Washington', 'Washington Wizards') for s in row]
        row = [s.replace('Orlando', 'Orlando Magic') for s in row]
        row = [s.replace('Oklahoma City', 'Oklahoma City Thunder') for s in row]
        row = [s.replace('LA Lakers', 'Los Angeles Lakers') for s in row]
        row = [s.replace('Houston', 'Houston Rockets') for s in row]
        row = [s.replace('Charlotte', 'Charlotte Hornets') for s in row]
        row = [s.replace('Detroit', 'Detroit Pistons') for s in row]
        row = [s.replace('San Antonio', 'San Antonio Spurs') for s in row]

        modified_rows.append(row)

with open('stats.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    for row in modified_rows:
        writer.writerow(row)
