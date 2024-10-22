import pandas as pd
from lol.config import engine

query = "SELECT * FROM champions"

df = pd.read_sql_query(query, engine)

print(df.head())