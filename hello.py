
# importing pandas module 
import pandas as pd 
import serial #bruges til at kommunikere med uart 
import serial.tools.list_ports #bruges til at kommunikere med uart 
from datetime import datetime

#Variable 
Motor = False
nuvaerende_dato_tid = datetime.now()

# making data frame 
data = pd.read_csv("nba.csv") #læser csv filen
print(data.head()) #printer top 5 lines i csv filen
print(data.tail())#printer bund 5 lines i csv filen



def StartMotor():
    Motor = True
print(nuvaerende_dato_tid)


