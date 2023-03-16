import pandas as pd

data = pd.read_csv("C:\\python\\csv\\video_games.csv")

filtered_row = data[ data["Title"].str.contains("Spider-Man")]

spider = {
    "Title" : filtered_row["Title"],
    "Platform" : filtered_row["Release.Console"]
}

spider_frame = pd.DataFrame(spider)
spider_frame.to_csv("spider.csv")
# spider.to_csv("spider_title.csv")S