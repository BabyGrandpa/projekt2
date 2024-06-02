import pandas as pd
import numpy as np
from csv import DictWriter
import datetime as dt
import time
import os
from flask import Flask, request, jsonify
import serial.tools.list_ports

class SensorData:
    #Test data (se test_data funktionen)
    temp = [20,21,23,21,25,11,14,13,17]
    wind = [4,5,6,10,1,3,2,5,10]
    time = ['16:10','16:15','16:20','16:25','16:30','16:35','16:40','16:45','16:50']
    date = ['27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024','27/04/2024']
    datas = ['temperatur', 'wind speed', 'current time', 'current date', 'Predicted power']

    #constructor, opretter csv-fil. 
    def __init__(self):
        self.file_path = 'SensorData.csv'
        self.columns = ['temperatur', 'wind speed', 'current time', 'current date', 'Predicted power']
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.file_path, index=False)  

    # dette er dataen der bliver gemt i csv filen
    def add_row(self, temp, wind, time, date, effect):

        new_row = pd.DataFrame([[temp, wind, time, date, effect]], columns=self.columns)
        df = pd.read_csv(self.file_path)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(self.file_path, index=False)
        

    #tilføjer test data
    def add_test_data(self):
        for i in range(8):
            self.add_row(self.temp[i], self.wind[i], self.time[i], self.date[i], 1)
    
    #returnere dato
    def get_date(self):
        date = dt.date.today()
        date_c = date.strftime('%d/%m/%Y')
        return date_c
    
    #returnere tid i timer og minutter
    def get_time(self):
        time = dt.datetime.now()
        time_c = time.strftime('%H:%M')
        return time_c
    
    # vindmøllens teoretiske effekt ud fra gennemsnitlig typisk industrivindmølle-værdier.  
    def effect(self,wind):
        #luftens densitet (kg/m^3):
        p = 1.225
        #Radius af rotorblade (meter):
        R = 20
        #gennemsnitlig vindhasstighed (m/s): 
        v = wind
        #effektkoefficient, (maks 0.59 (Betz'lov))
        Cp = 0.59
        effect = 1/2*Cp*p*(R**2*(np.pi))*v**3
        return effect
    
    #returnere seneste datamåling
    def get_latest(self):
        df = pd.read_csv('SensorData.csv')
        return df.tail(1)
    
    #returnere seneste 10 datamålinger
    def get_10(self):
        df = pd.read_csv('SensorData.csv')
        return df.tail(10)
    
    #returnere seneste 100 datamålinger
    def get_100(self):
        df = pd.read_csv('SensorData.csv')
        return df.tail(100)  
    
    #def UART(self):
        ser = serial.Serial(port='COM10',\
                            baudrate=57600,\
                            parity=serial.PARITY_NONE,\
                            stopbits=serial.STOPBITS_ONE,\
                            bytesize=serial.EIGHTBITS,\
                            timeout=0)

        data_l = []

        while True:
            # Læser alle indgående bytes
            for packet in ser.read():
                # Alle de læste bytes bliver lagret i data_l listen, og bliver converteret ind til char variabler
                data_l.append(chr(packet))
                # Hvis den læste variable sendt fra PSoC er et S, starter convertions processen
                if chr(packet) == 'S':
                    # Alle elementer i data_l bliver sadt ind i variablen data, og konvertere alle char til en string
                    data = ''.join([str(data) for data in data_l])
                    # Der printes data hvorefter stringen bliver splittet alle stederne med ", " hvor førte element efter ", " er vind og anden element er temperatur
                    print("\nData:", data)
                    wind = data.split(", ")[1]
                    temp = data.split(", ")[2]
                    print("wind:", wind)
                    print("temp:", temp)
                    # Den oversatte sensordata bliver passeret gennem add_row() funktionen som en float istedet for en string, 
                    # og variblerne data_l og data bliver tømt så det er klar til næste læsning
                    self.add_row(float(temp),float(wind), self.get_time(), self.get_date(), self.effect(wind))
                    data_l = []
                    data = "" 
        ser.close()
        
    
Sensor = SensorData()

Sensor.add_test_data()
Sensor.add_row(1,1,Sensor.get_time(),Sensor.get_date(),1)
#print(Sensor.effect(), "watt")
#print(Sensor.get_latest())
#print(Sensor.get_last10temp())



