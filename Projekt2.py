import pandas as pd
import serial
import serial.tools.list_ports
from datetime import datetime, date
import numpy as np


#Ved hjælp af self kan du 
#tilgå og manipulere disse værdier individuelt for hver instans.
class Tid_Dato:
    def __init__(self):
        self.nuvaerende_dato = date.today() 
        self.nuvaerende_tid = self.get_current_time()

    @staticmethod 
    def get_current_time():
        now = datetime.now()
        time_without_seconds = now.strftime('%H:%M')
        return time_without_seconds
    
    

    def udskriv_data(self):
        print(self.nuvaerende_dato, self.nuvaerende_tid)

    def CSV(self, filnavn):
        #nøgle er "Dato", der repræsentere kolonne overskrift: 
        #[self.nuvarende_dato/tid] er en liste der indeholder en værdi
        data = {
        "Dato": [self.nuvaerende_dato],
        "Tid": [self.nuvaerende_tid],
        }
        dataframe = pd.DataFrame(data)

        #lav dataframen til en csv-fil
        dataframe.to_csv(filnavn, index = False, encoding='utf-8')
        #index=False for ikke at inkludere rækkeindex i filen
    
S1=Tid_Dato()
S1.udskriv_data()
S1.CSV("Tid_Dato")

   

    


