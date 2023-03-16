import pandas as pd

scraper = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")


# for idx, table in enumerate(scraper):
#     print("****************")
#     print(idx)
#     print(table)

print(scraper[3])