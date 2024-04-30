import pandas as pd


dread = pd.read_csv("SensorData.csv", header = 0, usecols=["temperatur","wind speed","current time", "current date", "within threshold"])

gk = dread.groupby('within threshold')
gr = gk.get_group('True')
print(gr)