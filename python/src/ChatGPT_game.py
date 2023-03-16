import random
import pprint
import csv
import os.path

class Game:
    def __init__(self, id, title, genre, year, platform):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year
        self.platform = platform
        self.score = random.randint(60, 100)

    def __str__(self):
        return f'{self.id}. {self.title} - {self.genre} - {self.year} - {self.platform} - {self.score}'
        
class GameLibrary:
    def __init__(self):
        self.games = []
        self.keys = ["id", "game_title", "game_genre", "game_year", "game_platform", "game_score"]

    def add_game(self, title, genre, year, platform):
        id = len(self.games) + 1
        game = Game(id, title, genre, year, platform)
        self.games.append(game)

    def get_games(self):
        return self.games

    def print_games(self):
        for game in self.games:
            print(game)

    def save_to_csv(self):
        game_file = "game_library_3.csv"
        file_path = os.path.isfile(f"C:\\src\\{game_file}")

        with open(game_file, "a") as game_csv:
            csvwriter = csv.DictWriter(game_csv, fieldnames = self.keys)
            if not file_path:
                csvwriter.writeheader()
            for game in self.games:
                csvwriter.writerow({
                    "id": game.id,
                    "game_title": game.title,
                    "game_genre": game.genre,
                    "game_year": game.year,
                    "game_platform": game.platform,
                    "game_score": game.score
                })

# Usage example:
library = GameLibrary()

user_game = ""
while user_game != "done":
    user_game = input("Please enter a game (or done to quit): ").lower()
    if user_game == "done":
        break

    user_genre = input("Enter genre: ")
    user_platform = input("Enter platform: ")
    user_year = input("Enter year: ")

    library.add_game(user_game, user_genre, user_year, user_platform)

library.print_games()
library.save_to_csv()