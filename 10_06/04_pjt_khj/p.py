import pandas as pd
A = 'weathers/data/austin_weather.csv'
csv = pd.read_csv(A)
print(csv.loc[:,'Date'])