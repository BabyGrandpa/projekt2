import pandas as pd
import numpy as np

class SensorData:
    temp = [20,21,23,21,25,11,14,13,17]
    wind = [4,5,6,10,1,3,2,5,10]
    time = ['16:10','16:15','16:20','16:25','16:30','16:35','16:40','16:45','16:50']
    date = ['27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024']

    dict = {'temperatur': temp, 'wind speed': wind, 'current time': time, 'current date':date}

something = SensorData()

df = pd.DataFrame(something.dict)
df.to_csv('file1.csv')

dread = pd.read_csv("SensorData.csv",header = 0, usecols=["temperatur","wind speed","current time", "current date"])
print(dread)