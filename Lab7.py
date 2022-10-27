import pandas as pd

city_temps = pd.read_csv("city_temperature.csv", sep = ",")

df = city_temps.loc[city_temps.groupby(['Region'])['AvgTemperature'].idxmax()]
print(df)
df.to_csv("city_maxtemp.csv")


