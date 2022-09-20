

import csv
from pathlib import Path

csv_file = Path("Premier 16-17.csv")


def check_file_exists(csv_file):
    return csv_file.is_file()


def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


def process_results(rows):
    dictionary = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0, 0, 0, 0, 0]

        if away not in dictionary:
            dictionary[away] = [0, 0, 0, 0, 0]

        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
            dictionary[home][3] += 1
            dictionary[away][3] += 1

        if winner == "A":
            dictionary[home][0] = dictionary[home][0]
            dictionary[away][0] += 3
            dictionary[away][2] += 1
            dictionary[home][4] += 1

        if winner == "H":
            dictionary[home][0] += 3
            dictionary[away][0] = dictionary[away][0]
            dictionary[home][2] += 1
            dictionary[away][4] += 1

        dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)
        dictionary[away][1] = dictionary[away][1] + int(awaygoals) - int(homegoals)

    return dictionary


file_contents = read_csv(csv_file)
sortedByPoints = {k: v for k, v in
                  sorted(process_results(file_contents).items(), key=lambda v: v[1][1] and v[1], reverse=True)}
print("")
print(f"{'Club':<30}{'PTS':<5}{'GD':<5}{'W':<5}{'D':<5}{'L':<5}")
print("")


def clubs_name(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    return clubs[i]


def totalPoints(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    names = clubs[i]
    return sortedByPoints[names][0]


def goalDifference(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    names = clubs[i]
    return sortedByPoints[names][1]


def wins(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    names = clubs[i]
    return sortedByPoints[names][2]


def draws(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    names = clubs[i]
    return sortedByPoints[names][3]


def loses(sortedByPoints):
    clubs = list(sortedByPoints.keys())
    names = clubs[i]
    return sortedByPoints[names][4]
