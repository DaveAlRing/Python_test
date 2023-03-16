import csv

with open("C:\\python\\csv\\game_test.csv") as gamefile:
    reader = csv.DictReader(gamefile)
    for row in reader:
        print(dict(row))
