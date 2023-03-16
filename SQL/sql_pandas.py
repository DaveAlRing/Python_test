import pandas as pd
from pandasql import sqldf
from pandasql import load_births

births = load_births()

print(sqldf("SELECT * FROM births WHERE births > 250000 LIMIT 5;", locals()))