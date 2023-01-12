import csv

with open('linear_regression.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

    coefficients = rows[1]

    intercept = float(coefficients[1])
    away_efg_coefficient = float(coefficients[2])
    away_tov_coefficient = float(coefficients[3])
    away_offensive_rebound_coefficient = float(coefficients[4])
    away_free_throw_rate_coefficient = float(coefficients[5])
    away_opponent_efg_coefficient = float(coefficients[6])
    away_opponent_tov_coefficient = float(coefficients[7])
    away_opponent_offensive_rebound_coefficient = float(coefficients[8])
    away_opponent_free_throw_rate_coefficient = float(coefficients[9])
    home_efg_coefficient = float(coefficients[10])
    home_tov_coefficient = float(coefficients[11])
    home_offensive_rebound_coefficient = float(coefficients[12])
    home_free_throw_rate_coefficient = float(coefficients[13])
    home_opponent_efg_coefficient = float(coefficients[14])
    home_opponent_tov_coefficient = float(coefficients[15])
    home_opponent_offensive_rebound_coefficient = float(coefficients[16])
    home_opponent_free_throw_rate_coefficient = float(coefficients[17])


def predict(away, home):
    with open('stats.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if row[0] == away:
                away_efg = float(row[3])
                away_tov = float(row[4])
                away_offensive_rebound = float(row[5])
                away_free_throw_rate = float(row[6])
                away_opponent_efg = float(row[8])
                away_opponent_tov = float(row[9])
                away_opponent_offensive_rebound = float(row[10])
                away_opponent_free_throw_rate = float(row[11])
            if row[0] == home:
                home_efg = float(row[3])
                home_tov = float(row[4])
                home_offensive_rebound = float(row[5])
                home_free_throw_rate = float(row[6])
                home_opponent_efg = float(row[8])
                home_opponent_tov = float(row[9])
                home_opponent_offensive_rebound = float(row[10])
                home_opponent_free_throw_rate = float(row[11])

    return intercept + (away_efg * away_efg_coefficient) + (away_tov * away_tov_coefficient) + (
                away_offensive_rebound * away_offensive_rebound_coefficient) + (
                away_free_throw_rate * away_free_throw_rate_coefficient) + (
                away_opponent_efg * away_opponent_efg_coefficient) + (
                away_opponent_tov * away_opponent_tov_coefficient) + (
                away_opponent_offensive_rebound * away_opponent_offensive_rebound_coefficient) + (
                away_opponent_free_throw_rate * away_opponent_free_throw_rate_coefficient) + (
                home_efg * home_efg_coefficient) + (home_tov * home_tov_coefficient) + (
                home_offensive_rebound * home_offensive_rebound_coefficient) + (
                home_free_throw_rate * home_free_throw_rate_coefficient) + (
                home_opponent_efg * home_opponent_efg_coefficient) + (
                home_opponent_tov * home_opponent_tov_coefficient) + (
                home_opponent_offensive_rebound * home_opponent_offensive_rebound_coefficient) + (
                home_opponent_free_throw_rate * home_opponent_free_throw_rate_coefficient)
