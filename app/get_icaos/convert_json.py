import pandas as pd

data = 'https://raw.githubusercontent.com/InfiniteFlightAirportEditing/Navigation/master/Fixes.json'

df = pd.read_json(data)

df = df.drop_duplicates()

df.to_excel(r'D:\DATAFILE.xlsx', index=None, header=True)
