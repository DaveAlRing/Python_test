import random
import pprint
import csv
import os.path

keys = ["id", "game_title", "game_genre", "game_year", "game_platform", "game_score"]

#empty lists to  hold user data
games = []
genre = []
platform = []
years = []

user_game = ""

#loop to collect data and append lists
while user_game != "done":

    user_game = input("Please enter a game (or done to quit): ").lower()
    if user_game == "done".lower():
        break
    
    user_genre = input("Enter genre: ")
    user_platform = input("Enter platform: ")
    user_year = input("Enter year: ")

    games.append(user_game)
    genre.append(user_genre)
    platform.append(user_platform)
    years.append(user_year)

#dictionary comprehension to combine collected data
game_library = [
    {
        key:(
            i if key == "id" 
            else games[i] if key == "game_title"
            else genre[i] if key == "game_genre"
            else years[i] if key == "game_year"
            else platform[i] if key == "game_platform"
            else random.randint(60, 100) if key == "game_score" #produces random score
            else None
            )
        for key in keys
    } 
    for i in range(len(games))
]

pprint.pprint(game_library)

game_file = "game_library_2.csv"
file_path = os.path.isfile(f"C:\\src\\{game_file}")

with open(game_file, "a") as game_csv:
    csvwriter = csv.DictWriter(game_csv, fieldnames = keys)
    if not file_path:
        csvwriter.writeheader()
    csvwriter.writerows(game_library)
