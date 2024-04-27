
# importing pandas module 
import pandas as pd 
import serial #bruges til at kommunikere med uart 
import serial.tools.list_ports #bruges til at kommunikere med uart 
from datetime import datetime
from datetime import date
import numpy as np

def get_current_time():
    now = datetime.now()
    time_without_seconds = now.strftime('%H:%M')
    return time_without_seconds

#Variable 
Motor = False
nuvaerende_dato = date.today()
nuvaerende_tid = get_current_time()



# making data frame 
data = pd.read_csv("nba.csv") #læser csv filen
print(data.head()) #printer top 5 lines i csv filen
print(data.tail())#printer bund 5 lines i csv filen

def StartMotor():
    Motor = True

print("dato:", nuvaerende_dato)
print("tid:", nuvaerende_tid)
arr = np.array([nuvaerende_dato, nuvaerende_tid])
print("Array:", "\n", arr)





