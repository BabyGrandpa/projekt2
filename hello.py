
# importing pandas module 
import pandas as pd 
import serial #bruges til at kommunikere med uart 
import serial.tools.list_ports #bruges til at kommunikere med uart 


# making data frame 
data = pd.read_csv("nba.csv") #læser csv filen
print(data.head()) #printer top 5 lines i csv filen

  
