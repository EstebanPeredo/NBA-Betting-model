import requests
import datetime
from bs4 import BeautifulSoup
from spread_picker import predict


def extract_odds_between_colins(s):
    start_index = s.index(':')
    end_index = s.index(':', start_index + 1)
    return s[start_index + 2:end_index]


def remove_tv_channel(s):
    s = s.replace('NBA TV', '')
    s = s.replace('ESPN', '')
    s = s.replace('TNT', '')
    s = s.replace('ABC', '')
    return s


def get_away_team(s):
    open_paren_index = s.find('(')

    if open_paren_index == -1:
        return s

    return s[:open_paren_index]


def get_home_team(s):
    home_team = []
    start = False
    for char in s:
        if start:
            if char == '(':
                break
            else:
                home_team.append(char)
        elif char == ')':
            start = True
    return ''.join(home_team)


def get_odds(s):
    if s == "":
        return ""
    odds = ""
    for char in s:
        if char.isdigit() or char == '-' or char == '.':
            odds += char
    return odds


def get_team(s):
    if s == 'Celtics' or s == 'BOS':
        s = s.replace('Celtics', 'Boston Celtics')
        s = s.replace('BOS', 'Boston Celtics')
    if s == 'Nets' or s == 'BKN':
        s = s.replace('Nets', 'Brooklyn Nets')
        s = s.replace('BKN', 'Brooklyn Nets')
    if s == 'Pelicans' or s == 'NO':
        s = s.replace('Pelicans', 'New Orleans Pelicans')
        s = s.replace('NO', 'New Orleans Pelicans')
    if s == 'Nuggets' or s == 'DEN':
        s = s.replace('Nuggets', 'Denver Nuggets')
        s = s.replace('DEN', 'Denver Nuggets')
    if s == 'Bucks' or s == 'MIL':
        s = s.replace('Bucks', 'Milwaukee Bucks')
        s = s.replace('MIL', 'Milwaukee Bucks')
    if s == 'Grizzlies' or s == 'MEM':
        s = s.replace('Grizzlies', 'Memphis Grizzlies')
        s = s.replace('MEM', 'Memphis Grizzlies')
    if s == 'Cavaliers' or s == 'CLE':
        s = s.replace('Cavaliers', 'Cleveland Cavaliers')
        s = s.replace('CLE', 'Cleveland Cavaliers')
    if s == '76ers' or s == 'PHI':
        s = s.replace('76ers', 'Philadelphia 76ers')
        s = s.replace('PHI', 'Philadelphia 76ers')
    if s == 'Clippers' or s == 'LAC':
        s = s.replace('Clippers', 'Los Angeles Clippers')
        s = s.replace('LAC', 'Los Angeles Clippers')
    if s == 'Mavericks' or s == 'DAL':
        s = s.replace('Mavericks', 'Dallas Mavericks')
        s = s.replace('DAL', 'Dallas Mavericks')
    if s == 'Suns' or s == 'PHX':
        s = s.replace('Suns', 'Phoenix Suns')
        s = s.replace('PHX', 'Phoenix Suns')
    if s == 'Kings' or s == 'SAC':
        s = s.replace('Kings', 'Sacramento Kings')
        s = s.replace('SAC', 'Sacramento Kings')
    if s == 'Trail Blazers' or s == 'POR':
        s = s.replace('Trail Blazers', 'Portland Trail Blazers')
        s = s.replace('POR', 'Portland Trail Blazers')
    if s == 'Pacers' or s == 'IND':
        s = s.replace('Pacers', 'Indiana Pacers')
        s = s.replace('IND', 'Indiana Pacers')
    if s == 'Heat' or s == 'MIA':
        s = s.replace('Heat', 'Miami Heat')
        s = s.replace('MIA', 'Miami Heat')
    if s == 'Jazz' or s == 'UTAH':
        s = s.replace('Jazz', 'Utah Jazz')
        s = s.replace('UTAH', 'Utah Jazz')
    if s == 'Knicks' or s == 'NY':
        s = s.replace('Knicks', 'New York Knicks')
        s = s.replace('NY', 'New York Knicks')
    if s == 'Warriors' or s == 'GS':
        s = s.replace('Warriors', 'Golden State Warriors')
        s = s.replace('GS', 'Golden State Warriors')
    if s == 'Hawks' or s == 'ATL':
        s = s.replace('Hawks', 'Atlanta Hawks')
        s = s.replace('ATL', 'Atlanta Hawks')
    if s == 'Timberwolves' or s == 'MIN':
        s = s.replace('Timberwolves', 'Minnesota Timberwolves')
        s = s.replace('MIN', 'Minnesota Timberwolves')
    if s == 'Bulls' or s == 'CHI':
        s = s.replace('Bulls', 'Chicago Bulls')
        s = s.replace('CHI', 'Chicago Bulls')
    if s == 'Raptors' or s == 'TOR':
        s = s.replace('Raptors', 'Toronto Raptors')
        s = s.replace('TOR', 'Toronto Raptors')
    if s == 'Thunder' or s == 'OKC':
        s = s.replace('Thunder', 'Oklahoma City Thunder')
        s = s.replace('OKC', 'Oklahoma City Thunder')
    if s == 'Wizards' or s == 'WSH':
        s = s.replace('Wizards', 'Washington Wizards')
        s = s.replace('WSH', 'Washington Wizards')
    if s == 'Lakers' or s == 'LAL':
        s = s.replace('Lakers', 'Los Angeles Lakers')
        s = s.replace('LAL', 'Los Angeles Lakers')
    if s == 'Magic' or s == 'ORL':
        s = s.replace('Magic', 'Orlando Magic')
        s = s.replace('ORL', 'Orlando Magic')
    if s == 'Spurs' or s == 'SA':
        s = s.replace('Spurs', 'San Antonio Spurs')
        s = s.replace('SA', 'San Antonio Spurs')
    if s == 'Rockets' or s == 'HOU':
        s = s.replace('Rockets', 'Houston Rockets')
        s = s.replace('HOU', 'Houston Rockets')
    if s == 'Hornets' or s == 'CHA':
        s = s.replace('Hornets', 'Charlotte Hornets')
        s = s.replace('CHA', 'Charlotte Hornets')
    if s == 'Pistons' or s == 'DET':
        s = s.replace('Pistons', 'Detroit Pistons')
        s = s.replace('DET', 'Detroit Pistons')
    return s


def get_substring_before_space(s):
    space_index = s.find(' ')

    if space_index == -1:
        return s

    return s[:space_index]


def make_pick(away_team, home_team, favorite, spread):
    if away_team == "" or home_team == "" or favorite == "" or spread == "":
        return ""
    prediction = predict(away_team, home_team)
    if favorite == away_team:
        if abs(prediction) > abs(float(spread)):
            return away_team + ' -' + str(abs(float(spread)))
        if abs(prediction) < abs(float(spread)):
            return home_team + ' +' + str(abs(float(spread)))
    if favorite == home_team:
        if abs(prediction) > abs(float(spread)):
            return home_team + ' -' + str(abs(float(spread)))
        if abs(prediction) < abs(float(spread)):
            return away_team + ' +' + str(abs(float(spread)))


def predictions():
    url = 'https://www.espn.com/nba/scoreboard/_/date/'
    today = datetime.datetime.now()
    date = today.strftime("%Y%m%d")
    response = requests.get(url + date)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    odds = soup.find_all(class_='Scoreboard bg-clr-white flex flex-auto justify-between')
    predictions = ""

    for odd in odds:
        away_team = get_team(remove_tv_channel(get_away_team(odd.text)))
        home_team = get_team(remove_tv_channel(get_home_team(odd.text)))
        favorite = get_team(get_substring_before_space(extract_odds_between_colins(odd.text)))
        spread = get_odds(extract_odds_between_colins(odd.text))
        predictions += str(make_pick(away_team, home_team, favorite, spread)) + "\n"
    return predictions.rstrip()


# print(predictions())
