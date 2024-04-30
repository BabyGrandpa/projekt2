import pandas as pd
import numpy as np
from csv import DictWriter
import datetime as dt

class SensorData:
    temp = [20,21,23,21,25,11,14,13,17]
    wind = [4,5,6,10,1,3,2,5,10]
    time = ['16:10','16:15','16:20','16:25','16:30','16:35','16:40','16:45','16:50']
    date = ['27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024']
    datas = ['temperatur', 'wind speed', 'current time', 'current date']

    dict = {'temperatur': temp, 'wind speed': wind, 'current time': time, 'current date':date}

    def add_row(self, a, b, c, d):
        better_dict = {'temperatur': a, 'wind speed': b, 'current time': c, 'current date': d}

        with open('SensorData.csv', 'a', newline='') as f_object:
            dict_writer = DictWriter(f_object, fieldnames=self.datas)
            dict_writer.writerow(better_dict)
    
    def get_date(Self):
        date = dt.date.today()
        date_c = date.strftime('%d/%m/%Y')
        return date_c
        
    def get_time(Self):
        time = dt.datetime.now()
        time_c = time.strftime('%H:%M')
        return time_c

something = SensorData()
df = pd.DataFrame(something.dict)
df.to_csv('SensorData.csv', index=False)

a = 17
b = 10
c = something.get_time()
d = something.get_date()

something.add_row(a,b,c,d)

dread = pd.read_csv("SensorData.csv", header = 0, usecols=["temperatur","wind speed","current time", "current date"])

gk = dread.groupby('wind speed')
gr = gk.get_group(10)
print(gr)