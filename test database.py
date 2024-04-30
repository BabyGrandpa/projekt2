import pandas as pd
import numpy as np
from csv import DictWriter
import datetime as dt
import time

class SensorData:
    temp = [20,21,23,21,25,11,14,13,17]
    wind = [4,5,6,10,1,3,2,5,10]
    time = ['16:10','16:15','16:20','16:25','16:30','16:35','16:40','16:45','16:50']
    date = ['27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024']
    datas = ['temperatur', 'wind speed', 'current time', 'current date', 'within threshold']

    def __init__(self):
        dict = {'temperatur': self.temp, 'wind speed': self.wind, 'current time': self.time, 'current date': self.date, 'within threshold': bool}
        df = pd.DataFrame(dict)
        df.to_csv('SensorData.csv', index=False)

    def add_row(self, a, b, c, d):
        better_dict = {'temperatur': a, 'wind speed': b, 'current time': c, 'current date': d,'within threshold': self.within_tresh(b,6,5)}

        with open('SensorData.csv', 'a', newline='') as f_object:
            dict_writer = DictWriter(f_object, fieldnames=self.datas)
            dict_writer.writerow(better_dict)
    
    def get_date(self):
        date = dt.date.today()
        date_c = date.strftime('%d/%m/%Y')
        return date_c
        
    def get_time(self):
        time = dt.datetime.now()
        time_c = time.strftime('%H:%M')
        return time_c
    
    def within_tresh(self, a, b, c):
        if (a <= b and a >= c ):
            return True
        return False

something = SensorData()

while 1:
    a = np.random.randint(10,25)
    b = np.random.randint(1,14)
    c = something.get_time()
    d = something.get_date()

    something.add_row(a,b,c,d)
    time.sleep(5)


dread = pd.read_csv("SensorData.csv", header = 0, usecols=["temperatur","wind speed","current time", "current date", "within threshold"])

gk = dread.groupby('within threshold')
gr = gk.get_group(True)
print(gr)